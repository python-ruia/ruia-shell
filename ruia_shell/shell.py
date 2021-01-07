#!/usr/bin/env python
"""
 Created by howie.hu at 2021/1/5.
"""
import asyncio
import logging

from typing import Union

from IPython.terminal.embed import InteractiveShellEmbed
from IPython.terminal.ipapp import load_default_config
from ruia import Request, Response

from ruia_shell.config import BANNER

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

    def __init__(self, user_ns: dict = None, python_shell: str = "ipython"):
        """
        Init var
        :param user_ns: user namespace,  set the default value to `None`
        :param python_shell: ipython only support
        """
        self.banner = BANNER
        self.user_ns = user_ns or {}
        self.python_shell = python_shell
        self.fetch = lambda x: asyncio.get_event_loop().run_until_complete(
            self.async_fetch(x)
        )

    async def async_fetch(self, url_or_request: Union[Request, str]):
        """
        Fetch target URL
        :param url_or_request:
        :return:
        """
        if isinstance(url_or_request, Request):
            request: Request = url_or_request
        else:
            request: Request = Request(url=url_or_request)

        response: Response = await request.fetch()
        # process response
        response.html = await response.text()
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

    def r_help(self):
        """
        Help func for Ruia shell.
        :return:
        """
        pass

    def start(
        self,
        url_or_request: Union[Request, str] = None,
        request: Request = None,
        response: Response = None,
    ):
        """
        Start a python shell for debugging
        :return:
        """
        if url_or_request:
            self.fetch(url_or_request)
        else:
            self.refresh_user_ns(request, response)

        # start python shell
        start_python_console(user_ns=self.user_ns, banner=self.banner)


# if __name__ == "__main__":
#     Shell().start("https://httpbin.org/get")
