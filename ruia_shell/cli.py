#!/usr/bin/env python
"""
 Created by howie.hu at 2021/1/7.
"""

import fire

from ruia_shell.shell import Shell


def ruia_shell(url: str):
    """
    Provide an easy way to debug the Ruia script.
    :param url:
    :return:
    """
    Shell().start(url)


def execute():
    fire.Fire(ruia_shell)
