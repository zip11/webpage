#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests

import json

import pyperclip

# zone id
zid1 = "9"

# api id
aut1 = "Bearer G"

# worker name
wnam1 = "git"

# worker 网址 路由
wwz1 = ""

def worker_list(zid:str,aut:str,wnam:str):

    '''
    :param zid:str zone id
    :param aut:str api key
    :param wnam:str worker name
    :return: str worker-id
    '''

    # worker 获取列表

    url = "https://api.cloudflare.com/client/v4/zones/" + zid + "/workers/routes"

    headers = {
        "Content-Type": "application/json",
        "Authorization": aut
    }

    response = requests.request("GET", url, headers=headers)

    # 应答 json格式
    zd = response.json()
    
    # print(zd)

    # worker 的数量
    print("worker 的数量",len(zd["result"]))

    # worker 的 id
    # print(zd["result"][4]["id"])
    # 'script': 'gitcf'

    # 循环 查找 worker 的id
    for index in range(len(zd["result"])):

        # 判断 worker 的 名字
        if zd["result"][index]['script']  == wnam :

            # 获取 worker id
            wid1 = zd["result"][index]['id']
            break             
    
    return wid1


def update_worker(zid:str,aut:str,rid:str,wwz:str,snam:str):

    '''
    :param zid:str zone id
    :param aut:str api key
    :param rid:str router-id
    :param wwz:str worker-link
    :param wnam:str worker-name
    :return: str worker-link-status-ok/error
    '''

    # 更新 worker 网址 路由

    url = "https://api.cloudflare.com/client/v4/zones/" + zid + "/workers/routes/" + rid

    payload = {
        "pattern": wwz,
        "script": snam
    }
    headers = {
        "Conteny-Type": "application/json",
        "Authorization": aut
    }

    response = requests.request("PUT", url, json=payload, headers=headers)

    print(response.text)

# 获取 worker id
wo_id = worker_list(zid1,aut1,wnam1)

print(wo_id)

# 更新 worker 路由 网址
update_worker(zid1,aut1,wo_id,wwz1,wnam1)



