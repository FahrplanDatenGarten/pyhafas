#!/usr/bin/env python3
"""Setup file for the HAFAS client."""
import os
import sys

import setuptools

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist upload')
    sys.exit()

setup(
    name='pyhafas',
    version='0.2.0',
    description='Python client for HAFAS public transport APIs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/n0emis/pyhafas',
    download_url='https://github.com/n0emis/pyhafas/releases',
    author='Simeon Keske, Leo Maroni',
    author_email='dev@n0emis.eu, hello@em0lar.de',
    license='MIT',
    install_requires=['requests==2.24.*',
                      'pycryptodome==3.9.*',
                      'pytz==2020.1'],
    packages=setuptools.find_packages(include=['pyhafas', 'pyhafas.*']),
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ],
)
