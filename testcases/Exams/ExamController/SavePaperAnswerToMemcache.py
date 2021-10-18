# import sys
# import os
# from pathlib import Path
# o_path = os.getcwd()
# sys.path.append(o_path)
# sys.path.insert(0, str(Path(__file__).parent.parent))

# from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

# from OpenPaper_test import TestOpenPaper


# class TestSavePaperAnswerToMemcache(HttpRunner):
#     config = (
#         Config("demo,获取课程信息")
#         .variables(HOST="${ENV(UtestHOST)}")
#         .base_url("${HOST}")
#         .verify(False)
#         .export(*[])
#     )
#     teststeps = [
#         Step(
#             RunTestCase('获取考试id')
#             .call(TestOpenPaper)
#             .export(*['OpenPaper'])
#         ),
#         Step(
#             RunRequest("答题记录")
#             .post("/exams/learner/savePaperAnswerToMemcache")
#             .with_headers(**{"Content-Type": "application/json","Authorization": "${ENV(stu001_token)}"})
#             .with_json({
#                 "autoSavedKey": "${get_list($OpenPaper,result.autoSavedKey)}",
#                 "costTime": "${get_list($OpenPaper,result.exam.createTime)}",
#                 "examUserId": "${get_list($OpenPaper,result.examUserId)}",
#                 "json": "{\"tabs\":[{\"ID\":12257859,\"answer\":\"A\",\"type\":1,\"score\":1},{\"ID\":12257620,\"answer\":[\"A\",\"B\",\"C\"],\"type\":2,\"score\":1},{\"ID\":12257909,\"answer\":\"true\",\"type\":4,\"score\":1},{\"ID\":12257715,\"answer\":[\"1\",\"1\",\"1\"],\"type\":3,\"score\":1},{\"ID\":12257956,\"answer\":\"1\",\"type\":5,\"score\":1},{\"ID\":12257693,\"answer\":[\"A\",\"B\",\"C\",\"D\"],\"type\":12,\"score\":1},{\"ID\":12257639,\"answer\":\"A\",\"type\":17,\"score\":1},{\"ID\":12257640,\"answer\":\"A\",\"type\":17,\"score\":1},{\"ID\":12257641,\"answer\":\"A\",\"type\":17,\"score\":1},{\"ID\":12257642,\"answer\":\"A\",\"type\":17,\"score\":1},{\"ID\":12257656,\"answer\":\"A\",\"type\":1,\"score\":1},{\"ID\":12257657,\"answer\":\"A\",\"type\":1,\"score\":1},{\"ID\":12257658,\"answer\":\"A\",\"type\":1,\"score\":1},{\"ID\":12257661,\"answer\":\"A\",\"type\":1,\"score\":1},{\"ID\":12257920,\"answer\":\"\",\"type\":19,\"score\":1},{\"ID\":12257921,\"answer\":\"\",\"type\":16,\"score\":1},{\"ID\":12257680,\"answer\":\"A\",\"type\":1,\"score\":1},{\"ID\":12257681,\"answer\":[\"A\",\"B\",\"C\"],\"type\":2,\"score\":1},{\"ID\":12257682,\"answer\":\"true\",\"type\":4,\"score\":1},{\"ID\":12257683,\"answer\":[\"1\"],\"type\":3,\"score\":1},{\"ID\":12257684,\"answer\":\"1\",\"type\":5,\"score\":1},{\"ID\":12257685,\"answer\":[\"A\",\"B\",\"C\",\"D\"],\"type\":12,\"score\":1},{\"ID\":12257790,\"answer\":[\"1\"],\"type\":25,\"score\":1,\"grade\":\"0.0\"},{\"ID\":12257605,\"answer\":\"A\",\"type\":1,\"score\":1},{\"ID\":12257955,\"answer\":[\"A\",\"B\",\"C\"],\"type\":2,\"score\":1},{\"ID\":12257915,\"answer\":\"A\",\"type\":17,\"score\":1}],\"surplus\":\"55:00\",\"endTime\":\"2021-8-22 12:2\"}"
#             })
#             .validate()
#             .assert_equal("status_code", 200)
#         )
#     ]
    

# if __name__ == "__main__":
#     TestSavePaperAnswerToMemcache().test_start()