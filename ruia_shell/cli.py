#!/usr/bin/env python
"""
 Created by howie.hu at 2021/1/7.
"""

import fire

from ruia_shell.shell import Shell


def ruia_shell(url_or_request):
    """
    Start a Ruia shell
    :param url_or_request:
    :return:
    """
    Shell().start(url_or_request)


def execute():
    fire.Fire(ruia_shell)
