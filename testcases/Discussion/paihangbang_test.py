# NOTE: Generated By HttpRunner v3.1.6
# FROM: har\paihangbang.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCasePaihangbang(HttpRunner):

    config = (
        Config("教师查看排行榜")
        .variables(HOST="${ENV(TestHOST)}")
        .base_url("${HOST}")
        .verify(False)
        .export(*['studentid'])
    )

    teststeps = [
        Step(
            RunRequest("/topic/rankingList")
            .get("/topic/rankingList")
            .with_params(
                **{
                    "pn": "1",
                    "ps": "10",
                    "ocId": "${ENV(LoginNameCourseAdmin_ocId)}",
                    "discussionId": "",
                    "teacherId": "${ENV(LoginNameCourseAdmin_userid)}",
                    "classId": "",
                    "orderBy": "",
                }
            )
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Authorization": "${ENV(LoginNameCourseAdmin_token)}"
                }
            )
            .extract()
            .with_jmespath("body.result.list[0].userid","studentid")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("按教师查询")                        # 按教师id
            .get("/topic/rankingScreen")
            .with_params(**{"ocId": "${ENV(LoginNameCourseAdmin_ocId)}", "screenId": "${ENV(LoginNameCourseAdmin_userid)}", "type": "1"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Authorization": "${ENV(LoginNameCourseAdmin_token)}"
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 1)
            .assert_equal("body.message", "成功")
        ),
        Step(
            RunRequest("按班级查询")                                # 按班级id
            .get("/topic/rankingScreen")
            .with_params(**{"ocId": "${ENV(LoginNameCourseAdmin_ocId)}", "screenId": "${ENV(LoginNameCourseAdmin_class1)}", "type": "1"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Authorization": "${ENV(LoginNameCourseAdmin_token)}"
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/topic/selectInfo")
            .get("/topic/selectInfo")
            .with_params(**{"ocId": "${ENV(LoginNameCourseAdmin_ocId)}", "discussionId": "", "type": "1"})
            .with_headers(
                **{
                    "Accept": "application/json, text/plain, */*",
                    "Authorization": "${ENV(LoginNameCourseAdmin_token)}"
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCasePaihangbang().test_start()
