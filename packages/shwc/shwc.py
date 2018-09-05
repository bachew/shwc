# -*- coding: utf-8 -*-
import copy
from cached_property import cached_property
from datetime import datetime
from lektor.pluginsystem import Plugin
from lektor.project import Project


class LanguageMixin(object):
    languages = [
        ('en', 'English'),
        ('zh', u'中文'),
    ]

    @property
    def lang_codes(self):
        return [l[0] for l in self.languages]

    @property
    def default_lang_code(self):
        return self.languages[0][0]

    @property
    def translated_lang_codes(self):
        return [l[0] for l in self.languages[1:]]


class PluginMixin(object):
    @cached_property
    def project(self):
        return Project.discover()

    @cached_property
    def alternatives(self):
        config = self.project.open_config()
        prefix = 'alternatives.'
        alts = []

        for section in config.sections():
            if section.startswith(prefix):
                alt = config.section_as_dict(section)
                alts.append(alt)

        return alts

    @cached_property
    def locales(self):
        locales = []

        for alt in self.alternatives:
            locales.append(alt['locale'])

        return locales

    @cached_property
    def primary_alternative(self):
        for alt in self.alternatives:
            if alt.get('primary'):
                return alt

        raise RuntimeError('No primary alternative')

    @property
    def primary_locale(self):
        return self.primary_alternative['locale']

    @cached_property
    def secondary_locales(self):
        locales = []

        for alt in self.alternatives:
            if not alt.get('primary'):
                locales.append(alt['locale'])

        return locales

    def locale_from_path(self, path):
        term_path = path + '/'

        for locale in self.secondary_locales:
            if term_path.startswith('/{}/'.format(locale)):
                return locale

        return self.primary_locale

    def change_path_locale(self, path, locale):
        if not path.startswith('/'):
            raise ValueError('path must start with slash')

        if not locale:
            raise ValueError('locale cannot be empty')

        if locale not in self.locales:
            raise ValueError('locale must be one of {!r}'.format(self.locales))

        old_locale = self.locale_from_path(path)

        if old_locale == locale:
            return path

        # TODO: see if can use alternative.url_prefix

        if path == '/':
            path_names = []
        else:
            path_names = path.split('/')[1:]

        if old_locale == self.primary_locale:
            return '/' + '/'.join([locale] + path_names)

        if not path_names:
            return path

        if locale == self.primary_locale:
            path_names = path_names[1:]
        else:
            path_names[0] = locale

        return '/' + '/'.join(path_names)


class ShwcPlugin(Plugin, PluginMixin):
    def on_setup_env(self, **extra):
        self.setup_jinja()

    def setup_jinja(self):
        env = self.env.jinja_env
        env.trim_blocks = True
        env.lstrip_blocks = True

    def on_process_template_context(self, context, **extra):
        alts = copy.copy(self.alternatives)
        path = context['this'].path

        for alt in alts:
            alt['path'] = self.change_path_locale(path, alt['locale'])

        context['alts'] = alts
        context['now'] = datetime.utcnow()
