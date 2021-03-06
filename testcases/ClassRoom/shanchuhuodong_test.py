# NOTE: Generated By HttpRunner v3.1.6
# FROM: har\shanchuhuodong.har
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseShanchuhuodong(HttpRunner):

    config = (
        Config("教师创建课堂")
        .variables(HOST="${ENV(TestHOST)}",APPHOST="${ENV(TestHOSTAPP)}")
        .verify(False)
        .export(*[])
    )


    teststeps = [
        
        Step(
            RunRequest("/wisdomClassroom/getClassroomList")
            .get("${HOST}/wisdomClassroom/getClassroomList")
            .with_params(
                **{
                    "ocId": "${ENV(LoginNameCourseAdmin_ocId)}",
                    "classId": "",
                    "teacherId": "${ENV(LoginNameCourseAdmin_userid)}",
                    "status": "",
                    "pageNum": "1",
                    "pageSize": "10",
                    "lang": "zh",
                }
            )
            .with_headers(
                **{
                    "Authorization": "${ENV(LoginNameCourseAdmin_token)}",
                    "Content-Type": "application/json"
                }
            )
            .extract()
            .with_jmespath("body.list[0].id","classroomid")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            
            RunRequest("/wisdomClassroom/getClassroomActivitys/${classroomid}")
            .get(
                "${HOST}/wisdomClassroom/getClassroomActivitys/${classroomid}"
            )
            .with_params(**{"pageSize": "999", "pageNum": "1"})
            .with_headers(
                **{
                    "AUTHORIZATION": "${ENV(LoginNameCourseAdmin_token)}"
                }
            )
            .extract()
            .with_jmespath("body.list[0].id","id")
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/newAttendance/deleteAttendance")
            .post("${APPHOST}/newAttendance/deleteAttendance")
            .with_headers(
                **{
                    "AUTHORIZATION": "${ENV(LoginNameCourseAdmin_token)}",
                    "Content-Type": "application/json;charset=UTF-8"
                }
            )
            .with_json({"attanceID": "${id}", "userID": "${ENV(LoginNameCourseAdmin_userid)}"})
            .validate()
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseShanchuhuodong().test_start()
