# ruia-shell

A [Ruia](https://github.com/howie6879/ruia) plugin for terminal debugging(IPython)

```shell script
>>> ruia_shell <URL>

            ✨ Write less, run faster(0.8.0).
__________      .__                .__           .__  .__
\______   \__ __|__|____      _____|  |__   ____ |  | |  |
 |       _/  |  \  \__  \    /  ___/  |  \_/ __ \|  | |  |
 |    |   \  |  /  |/ __ \_  \___ \|   Y  \  ___/|  |_|  |__
 |____|_  /____/|__(____  / /____  >___|  /\___  >____/____/
        \/              \/       \/     \/     \/

Available variables:
    response            :   ruia.Response
    request             :   ruia.Request
    Spider              :   ruia.Spider

Available functions:
    fetch(url_or_req)   :   Fetch a URL or ruia.Request
    rhelp()             :   Tips for use
```

## Installation

```shell script
pip install -U ruia-shell
```

## Usage

This plugin provide an easy way to debug you [Ruia](https://github.com/howie6879/ruia) script:

```shell script
>>> ruia_shell http://httpbin.org/get

            ✨ Write less, run faster(0.8.0).
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

In [1]: request
Out[1]: <GET http://httpbin.org/get>

In [2]: response
Out[2]: <Response url[GET]: http://httpbin.org/get status:200>
```

Enjoy it :)