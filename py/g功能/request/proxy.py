import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
# post的数据
data = {"info": "biu~~~ send post request"}

# 代理信息,由快代理赞助
proxy = '115.203.28.25:16584'

proxies = {
    "http": "socks5://%(proxy)s/" % {'proxy': proxy},
    "https": "socks5://%(proxy)s/" % {'proxy': proxy}
}

# proxies = {
#     "http": "http://%(proxy)s/" % {'proxy': proxy},
#     "https": "http://%(proxy)s/" % {'proxy': proxy}
# }

r = requests.post('http://dev.kdlapi.com/testproxy', headers=headers, data=data, proxies=proxies) #加一个proxies参数
print(r.status_code)
print(r.text)