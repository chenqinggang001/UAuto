import sys
import os
from pathlib import Path
o_path = os.getcwd()
sys.path.append(o_path)
sys.path.insert(0, str(Path(__file__).parent.parent))

import pymysql

from debugtalk import GetEnvlist

# 数据连接信息:数据库对应的接口地址
class DBfunction():
    # def __init__(self):
        
    #     self.DBCONFIG = {
    #         "host":"114.116.232.197",
    #         "port": 3306,
    #         "user": "ulearningdb",
    #         "password": "ulearning_2015",
    #         "db": "ulearningdb"
    #     }

    # DBCONFIG = {
    #         "host":"114.116.232.197",
    #         "port": 3306,
    #         "user": "ulearningdb",
    #         "password": "ulearning_2015",
    #         "db": "ulearningdb"
    #     }
    def query(self):
        """
            方法：连接并且操作mysql数据库
            条件：根据env文件的TestHOST来判断用哪个数据库
            参数：sql: "select * from t_user where id=123"
            返回值： 
                ((id, username, password...), (id2, username2, passwor2,...))
        """
        if GetEnvlist.get_env(GetEnvlist,keyId='TestHOST') == 'courseapi.tongshike.cn':

            DBCONFIG = {
                "host":"119.3.253.124",
                "port": 3306,
                "user": "ulearningdb",
                "password": "ulearning_2015",
                "db": "ulearningdb"
            }
        
        elif GetEnvlist.get_env(GetEnvlist,keyId='TestHOST') == 'courseapi.ulearning.cn':
            DBCONFIG = {
                "host":"114.116.232.197",
                "port": 3306,
                "user": "ulearningdb",
                "password": "ulearning_2015",
                "db": "ulearningdb"
            }
        # 步骤1：连接并且打开对应的数据库
        db = pymysql.connect(host=DBCONFIG["host"], port=DBCONFIG["port"], user=DBCONFIG["user"], password=DBCONFIG["password"], db=DBCONFIG["db"])
        # 步骤2：获取查询的窗口：游标
        cur = db.cursor()
        # 步骤3：执行sql语句
        cur.execute(self)
        # 步骤4：获取对应的结果
        res = cur.fetchall()
        # 步骤5：关闭数据库连接
        db.close()

        return res

    # # 测试方法是否通过，注释代码
    # sql = "select userid from u_user_tab where loginName='chenqinggangtea'"
    # a = query(sql)
    # a1 = a[0][0]
    # print(a1)
    # print(len(str(a1)))