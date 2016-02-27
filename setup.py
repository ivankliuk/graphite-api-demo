#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

import graphite_api_plugin

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name="graphite_api_plugin",
    version=graphite_api_plugin.__version__,
    packages=["graphite_api_plugin"],
    description=graphite_api_plugin.__doc__,
    author=graphite_api_plugin.__author__,
    author_email=graphite_api_plugin.__email__,
    license=graphite_api_plugin.__license__,
    url=graphite_api_plugin.__url__,
    long_description=long_description,
    platforms=["any"],
    keywords=["graphite", "graphite-api"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: System :: Monitoring"],
    zip_safe=False)
