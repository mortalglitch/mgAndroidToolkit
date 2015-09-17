try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'mgAndroid Toolkit',
    'author': 'Joshua Neeley',
    'url': 'http://omegaraven.com',
    'download_url': 'na',
    'author_email': 'mortal.glitch@omegaraven.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['mgATK'],
    'scripts': [],
    'name': 'mgATK'
}

setup(**config)
