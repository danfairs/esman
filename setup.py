try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.0.1'

setup(
    name='esman',
    version=VERSION,
    description='Utilities for managing Elasticsearch',
    author='Dan Fairs',
    author_email='dan@secondsync.com',
    install_requires=[
        'pyes',
    ],
    entry_points={
        'console_scripts': [
            'esm = esman.cli:main'
        ]
    }
)
