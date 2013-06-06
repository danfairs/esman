try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='esman',
    description='Utilities for managing Elasticsearch',
    author='Dan Fairs',
    author_email='dan@secondsync.com',
    install_requires=[
        'pyes',
    ]
)
