import time
import sys
import os
from pathlib import Path
import jmespath
o_path = os.getcwd()
sys.path.append(o_path)
sys.path.insert(0, str(Path(__file__).parent.parent))
from httprunner import __version__, runner
sys.path.append('.env')
from GetAPI.Userlogin import *



def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

def get_Nowtime():
    Nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return Nowtime

# jmespath方法封装
def get_list(k,v):
    result = jmespath.search(str(v),k)
    return result

def get_list2(k,v):
    result = jmespath.search(str(v),k)
    s = result.strip(';')
    s2 = int(s)
    return s2

def steup_hook_test(request):
    print(request)

# 课堂活动单接口方法,返回type为n的活动
def group_list(ls,n):
    for i in ls:
        if i["relationType"] == n:
            return i["relationId"]


def setup_hook_delparams(request,param):
    if param in request['params']:
        request['params'] = request['params'].pop(param)

def wite_env():


    d1 = get_teaclassid('LoginNameCourseAdmin')
    d2 = get_stuclassid('stu001')
    d3 = get_stuclassid('stu015')
    d4 = get_stuclassid('stu020')

    # 用户信息解包，合并成字典到res
    res = Merge(d1,d2,d3,d4)
    print(res)
    for k,v in dict.items(res):
        os.environ[k] = str(v)

wite_env()

def get_osenv(key):
    return os.environ[key]
