#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

history = ""

requirements = [
    "pyramid>=1.7a2",
     "waitress"
]

test_requirements = [

]

extras_require = {
    
}

setup(
    name='src',
    version='0.1.4',
    description="Siyavula Education TodoList Application",
    long_description=readme + '\n\n' + history,
    author="Brian Mafu",
    author_email='brianmafu@gmail.com',
    packages=[
        'src',
    ],
    package_dir={'src':
                 'src'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='pyramid sms',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Pyramid',
    ],
    test_suite='tests',
    setup_requires=[
        "pytest-runner",
        # 'setuptools-git >= 0',
        # 'setuptools-git-version',
    ],
    tests_require=test_requirements,
    extras_require=extras_require,
)