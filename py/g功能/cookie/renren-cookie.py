#encoding=utf-8
#import urllib2 #ModuleNotFoundError: No module named 'urllib2'
import urllib.request

import urllib
#import cookielib #ModuleNotFoundError: No module named 'cookielib'
import http.cookiejar

def renrenBrower(url,user,password):
    #登陆页面，可以通过抓包工具分析获得，如fiddler，wireshark
    #login_page用户名及密码post提交的目标url，也可以用网页打开登录地址F12查看form表单的action地址，或netwrok里面查看提交地址
    login_page = "http://www.renren.com/PLogin.do"
    try:
        # 创建cookiejar实例对象
        #cookie = http.cookiejar.CookieJar()
        cookie = http.cookiejar.MozillaCookieJar("cookie.txt") #这个用于保存cookies
        
        #cookie = cookiejar.MozillaCookieJar() #读取cookies
        #cookie.load("cookie.txt")

        print(cookie)
        # <CookieJar[]>

        # 创建管理器
        cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
        http_handler = urllib.request.HTTPHandler()
        https_handler = urllib.request.HTTPSHandler()
        # 创建请求求管理器
        opener = urllib.request.build_opener(cookie_handler, http_handler, https_handler)


        #获得一个cookieJar实例
        #cj = cookielib.CookieJar()
        #cj = http.cookiejar.CookieJar()
        #cookieJar作为参数，获得一个opener的实例
        #opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        #opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))



        
        #伪装成一个正常的浏览器，避免有些web服务器拒绝访问。
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        #生成Post数据，含有登陆用户名密码。
        #data = urllib.urlencode({"email":user,"password":password})
        #urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)
        data = urllib.parse.urlencode({"email":user,"password":password}).encode('utf-8')  # 提交类型不能为str，需要为byte类型
        # email 及password 是表单的名字浏览器F12里面查看，另外有些站点需要提交csrf隐藏表单

        #以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie
        opener.open(login_page,data)
        #以带cookie的方式访问页面
        op=opener.open(url)

        print(cookie)
        cookie.save()
        #读取页面源码
        data= op.read().decode("UTF-8")
        return data
    except Exception as e:
        print(str(e))
#访问某用户的个人主页，其实这已经实现了人人网的签到功能。

#result = renrenBrower("http://www.renren.com/home","用户名","密码")
#
#我们想要获取登录后的http://www.renren.com/309365594/profile?v=info_timeline页面的内容
result = renrenBrower("http://www.renren.com/309365594/profile?v=info_timeline","xxxx@163.com","mima123446")

print(result)