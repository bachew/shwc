# -*- coding: utf-8 -*-
from unittest import TestCase
from shwc import PluginMixin


class PluginMixinTest(TestCase):

    def test_locale_from_path(self):
        mix = PluginMixin()
        resolve = mix.locale_from_path
        self.assertEqual('en', mix.primary_locale)
        self.assertEqual('en', resolve('/'))
        self.assertEqual('en', resolve('/welcome'))
        self.assertEqual('en', resolve('/zhizhi'))
        self.assertEqual('zh', resolve('/zh'))
        self.assertEqual('zh', resolve('/zh/'))
        self.assertEqual('zh', resolve('/zh/faq'))

    def test_change_path_language(self):
        mix = PluginMixin()
        self.assertEqual('en', mix.primary_locale)
        self.assertEqual('/', mix.change_path_locale('/', 'en'))
        self.assertEqual('/', mix.change_path_locale('/zh', 'en'))
        self.assertEqual('/zh', mix.change_path_locale('/', 'zh'))
        self.assertEqual('/zh', mix.change_path_locale('/zh', 'zh'))
