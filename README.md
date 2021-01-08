# ruia-shell

A [Ruia](https://github.com/howie6879/ruia) plugin for terminal debugging(IPython)

## Installation

```shell script
pip install -U ruia-shell
```

## Usage

This plugin provide an easy way to debug you [Ruia](https://github.com/howie6879/ruia) script:

```shell script
>>> ruia_shell https://movie.douban.com/top250

            ✨ Write less, run faster(0.8.0).
__________      .__                .__           .__  .__
\______   \__ __|__|____      _____|  |__   ____ |  | |  |
 |       _/  |  \  \__  \    /  ___/  |  \_/ __ \|  | |  |
 |    |   \  |  /  |/ __ \_  \___ \|   Y  \  ___/|  |_|  |__
 |____|_  /____/|__(____  / /____  >___|  /\___  >____/____/
        \/              \/       \/     \/     \/

Available Objects   :
    response            :   ruia.Response
    request             :   ruia.Request

Available Functions :
    attr_field          :   Extract attribute elements by using css selector or xpath
    text_field          :   Extract text elements by using css selector or xpath
    fetch               :   Fetch a URL or ruia.Request

In [1]: request
Out[1]: <GET https://movie.douban.com/top250>

In [2]: response
Out[2]: <Response url[GET]: https://movie.douban.com/top250 status:200>

In [3]: text_field(css_select="span.title")
Out[3]: '肖申克的救赎'

In [4]: attr_field(css_select="div.pic>a>img", attr="src")
Out[4]: 'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg'
```

Enjoy it :)