#!/usr/bin/env python3.6
from distutils.core import setup

setup(name='titanic',
      version='1.0',
      description="Analyze Kaggle's Titanic dataset and build a predictive model for the Titanic data science challenge",
      author='Daniel Lee',
      author_email='danielhanbitlee@gmail.com',
      url='',
      packages=['titanic'],
      install_requires=[
	'pypandoc>=1.4'
      ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
     )
