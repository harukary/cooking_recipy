# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

setup(
    name='recipy',
    version='0.1',
    description='Python package for cooking recipe structuring',
    author='Harukary',
    author_email='harukary7518@gmail.com',
    # install_requires=['numpy'],
    url='https://github.com/harukary/recipy',
    packages=find_packages(exclude=('tests', 'docs'))
)

