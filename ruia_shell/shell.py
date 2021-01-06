#!/usr/bin/env python
"""
 Created by howie.hu at 2021/1/5.
"""
from typing import Union

import ruia

from IPython.terminal.embed import InteractiveShellEmbed
from ruia import Request, Response, Spider

from ruia_shell.config import BANNER


class Shell:
    """
    Shell class to debug Ruia crawler script.
    """

    def __init__(self, user_ns: dict = None, python_shell: str = "ipython"):
        """
        Init var
        :param user_ns: user namespace,  set the default value to `None`
        :param python_shell: ipython only support
        """
        self.banner = BANNER
        self.user_ns = user_ns or {}
        self.python_shell = python_shell

    def fetch(self, url_or_request: Union[Request, str]):
        """
        Fetch target URL
        :param url_or_request:
        :return:
        """
        pass

    def refresh_user_ns(self):
        """
        Refresh the user namespace
        :return:
        """
        pass

    def r_help(self):
        """
        Help func for Ruia shell.
        :return:
        """
        pass

    def start(self):
        """
        Start a python shell for debugging
        :return:
        """
        pass
