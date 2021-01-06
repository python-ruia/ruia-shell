#!/usr/bin/env python
"""
 Created by howie.hu at 2021/1/4.
"""
import platform

import IPython
import ruia

from IPython import embed
# First import the embed function
from IPython.terminal.embed import InteractiveShellEmbed
from IPython.terminal.ipapp import load_default_config

# Now create the IPython shell instance. Put ipshell() anywhere in your code
# where you want it to open.
banner = f"""
            ✨ Write less, run faster({ruia.__version__}). 
__________      .__                .__           .__  .__   
\______   \__ __|__|____      _____|  |__   ____ |  | |  |  
 |       _/  |  \  \__  \    /  ___/  |  \_/ __ \|  | |  |  
 |    |   \  |  /  |/ __ \_  \___ \|   Y  \  ___/|  |_|  |__
 |____|_  /____/|__(____  / /____  >___|  /\___  >____/____/
        \/              \/       \/     \/     \/           

Available variables:
    response            :   ruia.Response
    request             :   ruia.Request
    spider              :   ruia.Spider

Available functions:
    fetch(url_or_req)   :   Fetch a URL or ruia.Request
    rhelp()             :   Tips for use
    
"""
exit_msg = "*** Back in main IPython ***"
InteractiveShellEmbed.clear_instance()
namespace = {"ruia": ruia}
ipshell = InteractiveShellEmbed.instance(
    banner1=banner, user_ns=namespace, exit_msg=exit_msg
)


ipshell()
