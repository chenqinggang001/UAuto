# NOTE: Generated By HttpRunner v3.1.6
# FROM: har\paihangbang-chakantiezi.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from pydantic.networks import import_email_validator

from paihangbang_test import TestCasePaihangbang


class TestCasePaihangbangChakantiezi(HttpRunner):

    config = (
        Config("教师账号排行榜查看帖子")
        .variables(HOST="${ENV(TestHOST)}")
        .base_url("${HOST}")
        .verify(False)
        .export(*[])
    )

    teststeps = [
        Step(
            RunTestCase('排行榜')
            .call(TestCasePaihangbang)
            .export('studentid')
        ),
        Step(
            RunRequest("/topic/selectInfo")
            .get("/topic/selectInfo")
            .with_params(**{"ocId": "${ENV(LoginNameCourseAdmin_ocId)}", "discussionId": "", "type": "4"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Authorization": "${ENV(LoginNameCourseAdmin_token)}"
                }
            )
            .extract()
            .with_jmespath("body.result[0].id","discussionId")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/post/integral")
            .get("/post/integral")
            .with_params(
                **{"ocId": "${ENV(LoginNameCourseAdmin_ocId)}", "discussionId": "$discussionId", "studentId": "$studentid"}
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Authorization": "${ENV(LoginNameCourseAdmin_token)}"
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.message", "成功")
        ),
        Step(
            RunRequest("/topic/findStudentPost")
            .get("/topic/findStudentPost")
            .with_params(
                **{
                    "pn": "1",
                    "ps": "10",
                    "userId": "$studentid",
                    "discussionId": "$discussionId",
                    "ocId": "${ENV(LoginNameCourseAdmin_ocId)}",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Authorization": "${ENV(LoginNameCourseAdmin_token)}"
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.message", "成功")
        ),
    ]


if __name__ == "__main__":
    TestCasePaihangbangChakantiezi().test_start()