#!/usr/bin/env python
"""
 Created by howie.hu at 2021/1/7.
"""

from setuptools import find_packages, setup

setup(
    name="ruia-shell",
    version="0.0.1",
    description="A Ruia plugin for terminal debugging(IPython)",
    install_requires=["fire", "ruia>=0.8.0", "ipython"],
    author="Howie Hu",
    author_email="xiaozizayang@gmail.com",
    url="https://github.com/python-ruia/ruia-shell",
    packages=find_packages(),
    entry_points={"console_scripts": ["ruia_shell = ruia_shell.cli:execute"]},
)
