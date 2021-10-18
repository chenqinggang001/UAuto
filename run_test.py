import os
# import pytest
# from allure_pytest import plugin as allure_plugin
# if __name__ == '__main__':
    # command_line = ["testcases/testcaseOBEEvaluationRuleDemo2", "--alluredir=results"]
    # pytest.main(command_line)

# args = ['testcases/testcaseOBEEvaluationRuleDemo2', '--alluredir=results']
# args = ['-s', '-v', '--alluredir=allure_result', test_path]
# pytest.main(args=args, plugins=[allure_plugin])
os.system('pytest testcases --alluredir=./results/xml --clean-alluredir')
os.system('allure generate ./results/xml -o ./reports/xml -c')
# os.system('allure generate results -o reports --clean')
# os.system('allure open -h 127.0.0.1 -p 12333 ./reports')
os.system('allure open ./reports/xml')