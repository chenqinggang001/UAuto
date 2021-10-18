
import sys
import os
from pathlib import Path

o_path = os.getcwd()
sys.path.append(o_path)
sys.path.insert(0, str(Path(__file__).parent.parent))
from debugtalk import GetEnvlist



class ActivityId(GetEnvlist):
    # def __init__(self,filepath,keyId):
    #     GetEnvlist.__init__(self,filepath,keyId)
    
    # # 获取活动id
    # def get_teaclassid(n):
    #     host = GetEnvlist.get_env(GetEnvlist,keyId='TestHOST')
    #     url = ""+host+"/classes"
    #     headers = {"Content-Type": "application/json","Authorization": UserLogin.get_userinfo("Adminteatoken")}
    #     param = {"ocId":get_ocId(),"pn":"1","ps":"10","userId":UserLogin.get_userinfo('AdminteauesrId'),"keyword":"","lang":"zh"}

    #     res = requests.get(url, headers=headers, params=param, verify=False)
    #     # 修正获取的班级id，以上面的注释为准
    #     if n == 0:
    #         n += 2
    #     elif n == 2:
    #         n -= 2
    #     print(res.json()['list'][n]['classId'])
    #     return res.json()['list'][n]['classId']
    pass
