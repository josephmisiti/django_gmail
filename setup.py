#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import django_gmail

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = django_gmail.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django_gmail',
    version=version,
    description="""Django integration of Gmails API""",
    long_description=readme + '\n\n' + history,
    author='Joseph Misiti',
    author_email='joseph.misiti@mathandpencil.com',
    url='https://github.com/josephmisiti/django_gmail',
    packages=[
        'django_gmail',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django_gmail',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
