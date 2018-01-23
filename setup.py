# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='vindinium-client',
    version='0.1.0',
    description='Client for Vindinium.org',
    long_description=readme,
    author='Sergey Petrunin',
    author_email='halfstrik@gmail.com',
    url='https://github.com/halfstrik/vendinium-client',
    license=license,
    packages=find_packages(),
    install_requires=['requests==2.18.4'],
)
