#!/usr/bin/env python
"""
 Created by howie.hu at 2021/1/5.
"""
import asyncio
import logging

from typing import Union

import nest_asyncio

from IPython.terminal.embed import InteractiveShellEmbed
from IPython.terminal.ipapp import load_default_config
from ruia import AttrField, Request, Response, Spider, TextField

from ruia_shell.config import BANNER

nest_asyncio.apply()

logging.getLogger("Ruia").setLevel(logging.WARNING)
logging.getLogger("Request").setLevel(logging.WARNING)


def start_python_console(user_ns: dict = None, banner: str = ""):
    """
    Start a python interactive terminal
    :param user_ns:
    :param banner:
    :return:
    """
    config = load_default_config()
    InteractiveShellEmbed.clear_instance()
    python_shell = InteractiveShellEmbed.instance(
        banner1=banner, user_ns=user_ns, config=config
    )

    python_shell()


class Shell:
    """
    Shell class to debug Ruia crawler script.
    """

    def __init__(
        self, spider: Spider = None, user_ns: dict = None, python_shell: str = "ipython"
    ):
        """
        Init var
        :param user_ns: user namespace,  set the default value to `None`
        :param python_shell: ipython only support
        """
        self.banner = BANNER
        self.user_ns = user_ns or {}
        self.python_shell = python_shell
        self.spider = spider
        if self.spider:
            loop = spider.loop
        else:
            loop = asyncio.get_event_loop()

        self.fetch = lambda x, y=None: loop.run_until_complete(self.async_fetch(x, y))

    async def async_fetch(
        self, url_or_request: Union[Request, str], response: Response = None,
    ):
        """
        Fetch target URL
        :param url_or_request:
        :param response:
        :return:
        """
        if isinstance(url_or_request, Request):
            request: Request = url_or_request
        else:
            request: Request = Request(url=url_or_request)

        if response is None:
            response: Response = await request.fetch()

        # process response
        response.html = await response.text()
        response.etree = response.html_etree(response.html)

        self.refresh_user_ns(request, response)

    def refresh_user_ns(self, request: Request, response: Response):
        """
        Refresh the user namespace
        :param request: ruia.Request
        :param response: ruia.Response
        :return:
        """
        import ruia

        self.user_ns["asyncio"] = asyncio
        self.user_ns["ruia"] = ruia
        self.user_ns["request"] = request
        self.user_ns["response"] = response
        self.user_ns["fetch"] = self.fetch
        self.user_ns["attr_field"] = lambda etree=response.etree, **kwargs: AttrField(
            **kwargs
        ).extract(etree)
        self.user_ns["text_field"] = lambda etree=response.etree, **kwargs: TextField(
            **kwargs
        ).extract(etree)

    def r_help(self):
        """
        Help func for Ruia shell.
        :return:
        """
        pass

    def start(
        self, url_or_request: Union[Request, str] = None, response: Response = None,
    ):
        """
        Start a python shell for debugging
        :return:
        """
        self.fetch(url_or_request, response)

        # start python shell
        start_python_console(user_ns=self.user_ns, banner=self.banner)


def inspect_ruia(
    spider: Spider, url_or_request: Union[Request, str], response: Response = None
):
    """
    Debugging in Ruia script
    :param spider:
    :param url_or_request:
    :param response:
    :return:
    """
    shell = Shell(spider)
    shell.fetch(url_or_request, response)
    # start python shell
    start_python_console(user_ns=shell.user_ns, banner=shell.banner)
