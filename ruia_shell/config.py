#!/usr/bin/env python
"""
 Created by howie.hu at 2021/1/6.
"""
import ruia

BANNER = f"""
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

Available functions:
    fetch(url_or_req)   :   Fetch a URL or ruia.Request
"""
#     spider              :   ruia.Spider
#    r_help()            :   Tips for use
