import sys
import os
from pathlib import Path

from pydantic.utils import IMMUTABLE_NON_COLLECTIONS_TYPES
o_path = os.getcwd()
sys.path.append(o_path)
sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.Exams.ExamController.OpenPaper_test import TestOpenPaper

class TestGetPaperForStudent(HttpRunner):
    config = (
        Config("demo,获取课程信息")
        .variables(HOST="${ENV(UtestHOST)}")
        .base_url("${HOST}")
        .verify(False)
        .export(*['examId'])
    )

    teststeps = [
        Step(
            RunTestCase('获取考试id')
            .call(TestOpenPaper)
            .export(*['OpenPaper'])
        ),
        Step(
            RunRequest("获取学生考试列表")
            .get("/exams/user/study/getPaperForStudent")
            .with_headers(**{"Content-Type": "application/json","Authorization": "${ENV(stu001_token)}"})
            .with_params(**{"examId": "${get_list($OpenPaper,result.exam.examId)}","paperId":"${get_list2($OpenPaper,result.exam.paperId)}","examUserId": "${get_list($OpenPaper,result.examUserId)}"})
            .with_json(
                {
                    "userId": "${ENV(stu001_userid)}" ,
                    "orgId": '${ENV(stu001_ocId)}'
                }
            )
            # .extract()
            # .with_jmespath("body.examList[0].examId", "examId")
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    TestGetPaperForStudent().test_start()