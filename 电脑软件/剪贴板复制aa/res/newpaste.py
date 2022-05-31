import requests
from requests.structures import CaseInsensitiveDict

def newpaste(api_paste_name,api_paste_code,api_dev_key,api_user_key):

    #新建 帖子 ，帖子标题 ，帖子 内容
    
    url = "https://pastebin.com/api/api_post.php"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"


    #帖子 标题
    #api_paste_name	= '1yw-';

    #帖子 内容
    #api_paste_code  = '1hj a bc';


    #api dev
    #api_dev_key = '';

    #用户 api
    #api_user_key = ''
    
    #帖子 公开
    api_paste_private = '0';

    #帖子 过期 时间
    api_paste_expire_date = 'N';



    data = "api_dev_key=" + api_dev_key + "&api_user_key=" + api_user_key + "&api_paste_code=" + api_paste_code + "&api_paste_name=" + api_paste_name + "&api_paste_expire_dat=" + api_paste_expire_date  + "&api_option=paste"


    resp = requests.post(url, headers=headers, data=data)

    
    print(resp.status_code)

    # http-code
    return resp.status_code

