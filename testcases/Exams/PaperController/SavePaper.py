from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
import sys
import os
from pathlib import Path
o_path = os.getcwd()
sys.path.append(o_path)
sys.path.insert(0, str(Path(__file__).parent.parent))


class SavePaper(HttpRunner):
    config = (
        Config("新增试卷")
        .variables(HOST="${ENV(UtestHOST)}")
        .base_url("${HOST}")
        .verify(False)
        .export(*[])
    )
    teststeps = [
        Step(
            RunRequest("新增试卷")
            .post("/papers/savePaper")
            .with_headers(**{"Content-Type": "application/json", "Authorization": "${ENV(stu001_token)}"})
            .with_json(
                {
                    "courseId": "${ENV(stu001_ocId)}",
                    "isShare": "string",
                    "orgId": 0,
                    "paperId": 0,
                    "paperPartDtoList": [
                        {
                            "examId": 0,
                            "orderIndex": 0,
                            "paperId": 0,
                            "paperPartId": 0,
                            "paperQuestionList": [
                                {
                                    "lisCount": 0,
                                    "orderIndex": 0,
                                    "paperId": 0,
                                    "paperPartId": 0,
                                    "questionDtos": [
                                        {}
                                    ],
                                    "questionId": 0,
                                    "questionParentId": 0,
                                    "score": 0
                                }
                            ],
                            "partDesc": "string",
                            "partName": "string",
                            "type": "string"
                        }
                    ],
                    "parentId": 0,
                    "score": 0,
                    "teacherIds": [
                        0
                    ],
                    "time": "string",
                    "title": "string",
                    "type": "string",
                    "userId": 0
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        )
    ]


if __name__ == "__main__":
    SavePaper().test_start()
