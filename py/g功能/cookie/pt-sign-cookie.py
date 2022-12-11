#encoding=utf-8

#pt登录 不支持 cf 5秒盾,不支持图片验证码

import requests


def renrenBrower(url,user,password):

    #登陆页面，可以通过抓包工具分析获得，如fiddler，wireshark
    #login_page用户名及密码post提交的目标url，也可以用网页打开登录地址F12查看form表单的action地址，或netwrok里面查看提交地址
    login_page = "https://123.com/takelogin.php"
    
    try:
        # 创建Session对象
        # requests库的session对象会在同一个session实例的所有请求之间使用cookies保持登录状态
        session = requests.Session()
    
        #伪装成一个正常的浏览器，避免有些web服务器拒绝访问。
        headers = {'User-agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}
        #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}


        #在session中发送登录请求，此后这个session里就存储了cookie
        #可以用print(session.cookies.get_dict())查看
        resp = session.post(login_page,{"username":user,"password":password})#post提交表单数据到登录地址
        # email 及password 是表单的名字浏览器F12里面查看，另外有些站点需要提交csrf隐藏表单

        resp = session.get(url,headers=headers)
        #携带cookies 以get方式访问目标url
        
        data = resp.content.decode('UTF-8')
        
        print(session.cookies.get_dict())
        
        return data

    except Exception as e:
        print(str(e))
#访问某用户的个人主页，其实这已经实现了人人网的签到功能。

#result = renrenBrower("http://www.renren.com/home","用户名","密码")
#我们想要获取登录后的http://www.renren.com/309365594/profile?v=info_timeline页面的内容
result = renrenBrower("https://123.com/","user","password")

print(result) 