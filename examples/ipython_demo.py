#!/usr/bin/env python
"""
 Created by howie.hu at 2021/1/4.
"""
import IPython
import ruia

from IPython import embed
# First import the embed function
from IPython.terminal.embed import InteractiveShellEmbed
from IPython.terminal.ipapp import load_default_config

# Now create the IPython shell instance. Put ipshell() anywhere in your code
# where you want it to open.
banner = "*** Nested interpreter ***"
exit_msg = "*** Back in main IPython ***"
InteractiveShellEmbed.clear_instance()
namespace = {"ruia": ruia}
ipshell = InteractiveShellEmbed.instance(
    banner1=banner, user_ns=namespace, exit_msg=exit_msg
)


ipshell()
