import sys
import os
from pathlib import Path

from pydantic.utils import IMMUTABLE_NON_COLLECTIONS_TYPES
o_path = os.getcwd()
sys.path.append(o_path)
sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.Exams.ExamController.OpenPaperFromOrg_test import TestOpenPaperFromOrg
from GetAPI.getIP import get_host_ip

class TestOpenPaper(HttpRunner):

    config = (
        Config("demo,获取课程信息")
        .variables(HOST="${ENV(UtestHOST)}")
        .base_url("${HOST}")
        .verify(False)
        .export(*['OpenPaper'])
    )
    teststeps = [
        Step(
            RunTestCase('获取考试id')
            .with_variables(HOST="${ENV(TestHOST)}")
            .call(TestOpenPaperFromOrg)
            .export(*['OpenPaperFromOrg'])
        ),
        Step(
            RunRequest("进入考试须知页面")
            .get("/exams/user/study/openPaper")
            .with_headers(**{"Content-Type": "application/json","Authorization": "${ENV(stu001_token)}"})
            .with_params(**{"examId":"${get_list($OpenPaperFromOrg,result.exam.examId)}","ip":get_host_ip(),"submitType":2,"token":""})
            .with_json(
                {
                    "userId":"${ENV(stu001_userid)}",
                    "orgId": '${ENV(stu001_ocId)}'
                }
            )
            .extract()
            .with_jmespath("body", "OpenPaper")
            .validate()
            .assert_equal("status_code", 200)
        )
    ]
    

if __name__ == "__main__":
    TestOpenPaper().test_start()