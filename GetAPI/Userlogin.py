
import sys
import os
from pathlib import Path
o_path = os.getcwd()
sys.path.append(o_path)
sys.path.insert(0, str(Path(__file__).parent.parent))

import requests

import urllib3
urllib3.disable_warnings()


def get_env(keyId):
    _dict = {}
    filepath = '.env'
    with open(filepath, 'r') as dict_file:
        for line in dict_file:
            (key, value) = line.strip().split('=')
            _dict[key] = value
        return _dict[keyId]


def get_userinfo(user):
    host = get_env('TestHOST')
    usernames = get_env(user)
    password = get_env('Password')
    url = host+"/users/login"
    body = {
            "loginName": usernames,
            "password": password
        }
    headers = {}
    res = requests.post(url, headers=headers, json=body, verify=False)
    token = res.json()["authorization"]
    userid = res.json()["userId"]
    s = {'%s_token'%user:token,'%s_userid'%user:userid}
    return s


def get_ocId(user):
    s = get_userinfo(user)
    host = get_env('TestHOST')
    url = host+"/courses"
    headers = {"Content-Type": "application/json","Authorization": s['%s_token'%user]}
    param = {"keyword":"","publishStatus":"1","type":"1","pn":"1","ps":"15","octypeId":"","lang":"zh"}
    res = requests.get(url, headers=headers, params=param, verify=False)

    v = res.json()["courseList"][0]["id"]
    s['%s_ocId'%user] = v
    return s

def get_stuocId(user):
    s = get_userinfo(user)
    host = get_env('TestHOST')
    url = host+"/courses/students"
    headers = {"Content-Type": "application/json","Authorization": s['%s_token'%user]}
    param = {"keyword":"","publishStatus":"1","type":"1","pn":"1","ps":"15","lang":"zh"}

    res = requests.get(url, headers=headers, params=param, verify=False)

    v = res.json()["courseList"][0]["id"]
    s['%s_ocId'%user] = v
    return s

def get_teaclassid(user):
    s = get_ocId(user)
    host = get_env('TestHOST')
    url = host+"/classes"
    headers = {"Content-Type": "application/json","Authorization": s['%s_token'%user]}
    param = {"ocId":s['%s_ocId'%user],"pn":"1","ps":"10","userId":s['%s_userid'%user],"keyword":"","lang":"zh"}

    res = requests.get(url, headers=headers, params=param, verify=False)

    v1 = res.json()['list'][0]['classId']
    v2 = res.json()['list'][1]['classId']
    v3 = res.json()['list'][2]['classId']
    s['%s_class1'%user] = v1
    s['%s_class2'%user] = v2
    s['%s_class3'%user] = v3
    return s

def get_stuclassid(user):
    s = get_stuocId(user)
    host = get_env('TestHOST')
    url = host+"/classes"
    headers1 = {"Content-Type": "application/json","Authorization": s['%s_token'%user]}
    param1 = {"ocId":s['%s_ocId'%user],"pn":"1","ps":"10","userId":s['%s_userid'%user],"keyword":"","lang":"zh"}
    res = requests.get(url, headers=headers1, params=param1, verify=False)
    v1 = res.json()['list'][0]['classId']
    s['%s_class'%user] = v1
    return s


def Merge(dict1, dict2 ,dict3 ,dict4): 
    res = {**dict1, **dict2, **dict3, **dict4} 
    return res 
