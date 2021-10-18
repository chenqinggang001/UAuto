import sys
import os
from pathlib import Path
o_path = os.getcwd()
sys.path.append(o_path)
sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.Exams.ExamController.GetStudentExamList_test import TestGetStudentExamList

class TestOpenPaperFromOrg(HttpRunner):
    config = (
        Config("进入考试须知页面")
        .variables(HOST="${ENV(TestHOST)}")
        .base_url("${HOST}")
        .verify(False)
        .export(*['OpenPaperFromOrg'])
    )
    teststeps = [
        Step(
            RunTestCase('获取考试id')
            .call(TestGetStudentExamList)
            .export(*['examId'])
        ),
        Step(
            RunRequest("进入考试须知页面")
            .get("/exams/user/study/openPaperFromOrg")
            .with_headers(**{"Content-Type": "application/json","Authorization": "${ENV(stu001_token)}"})
            .with_params(**{"examId":"${examId}","fromWhere":"1"})
            .extract()
            .with_jmespath("body","OpenPaperFromOrg")
            .validate()
            .assert_equal("status_code", 200)
        )
    ]

if __name__ == "__main__":
    TestOpenPaperFromOrg().test_start()