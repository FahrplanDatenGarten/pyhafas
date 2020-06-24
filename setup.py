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
    version='0.0.0.dev1',
    description='Python client for HAFAS public transport APIs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/n0emis/pyhafas',
    download_url='https://github.com/n0emis/pyhafas/releases',
    author='Simeon Keske, Leo Maroni',
    author_email='simeon@noemis.me, hello@em0lar.de',
    license='EUPL 1.2',
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ],
)
