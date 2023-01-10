#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#!/usr/bin/env python3

import os

print("bash run ok, cmd run error")

# bing search

ml1 = '''
  curl 'https://cn.bing.com/' \
  -H 'authority: cn.bing.com' \
  -H 'cache-control: max-age=0' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: none' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'accept-language: zh-CN,zh;q=0.9' \
  -H 'cookie: '\
  --compressed
'''

print(ml1)

var=os.popen(ml1).read( )

print(var)
