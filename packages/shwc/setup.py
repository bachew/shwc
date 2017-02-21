from setuptools import setup

setup(
    name='lektor-shwc',
    version='0.1',
    author=u'Chew Boon Aik,,,',
    author_email='bachew@gmail.com',
    license='MIT',
    py_modules=['lektor_shwc'],
    entry_points={
        'lektor.plugins': [
            'shwc = lektor_shwc:ShwcPlugin',
        ]
    }
)
