import sys
import os
from pathlib import Path
o_path = os.getcwd()
sys.path.append(o_path)
sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.Exams.ExamController.OpenPaper_test import TestOpenPaper


class TestGetExamReport(HttpRunner):
    config = (
        Config("demo,获取课程信息")
        .variables(HOST="${ENV(UtestHOST)}")
        .base_url("${HOST}")
        .verify(False)
        .export(*[])
    )
    teststeps = [
        Step(
            RunTestCase('获取考试id')
            .call(TestOpenPaper)
            .export(*['OpenPaper'])
        ),
        Step(
            RunRequest("答题记录")
            .get("/exams/user/study/examReport")
            .with_headers(**{"Content-Type": "application/json","Authorization": "${ENV(stu001_token)}"})
            .with_params(**{"examId":"${get_list($OpenPaper,result.exam.examId)}","examUserId":"${get_list($OpenPaper,result.examUserId)}"})
            .with_json({
                "userId":"${ENV(stu001_userid)}",
                "orgId":"${get_list($OpenPaper,result.exam.orgId)}",
                "roleId":9
            })
            .validate()
            .assert_equal("status_code", 200)
        )
    ]
    

if __name__ == "__main__":
    TestGetExamReport().test_start()