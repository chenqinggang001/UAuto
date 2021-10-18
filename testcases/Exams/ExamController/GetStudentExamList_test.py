import sys
import os
from pathlib import Path

from pydantic.utils import IMMUTABLE_NON_COLLECTIONS_TYPES
o_path = os.getcwd()
sys.path.append(o_path)
sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestGetStudentExamList(HttpRunner):
    config = (
        Config("demo,获取课程信息")
        .variables(HOST="${ENV(TestHOST)}")
        .base_url("${HOST}")
        .verify(False)
        .export(*['examId'])
    )

    teststeps = [
        Step(
            RunRequest("获取学生考试列表")
            .get("/exams/student")
            .with_headers(**{"Content-Type": "application/json","Authorization": "${ENV(stu001_token)}"})
            .with_params(**{"pn":"","ps":"1","ocId": "${ENV(stu001_ocId)}","userId": "${ENV(stu001_userid)}"})
            .extract()
            .with_jmespath("body.examList[0].examId", "examId")
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestGetStudentExamList().test_start()