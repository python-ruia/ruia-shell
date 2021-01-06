#!/usr/bin/env python
"""
 Created by howie.hu at 2021/1/5.
"""

from ruia import Request, Response, Spider


class Shell:
    """
    Shell class to debug Ruia crawler script.
    """

    def __init__(self, python_shell: str = "ipython"):
        """
        Init var
        :param python_shell: ipython only support
        """
        self.banner = ""

    def fetch(self, url: str):
        """
        Fetch target URL
        :param url:
        :return:
        """
        pass
