import unittest
from config.all_path import case_api_dir, project_path, report_dir
from common.BeautifulReport.BeautifulReport import BeautifulReport
from common.do_config import report_name, upload_MeterShpere, upload_robot, upload_email
from common.upload_report import insert_report, get_file_url
from common.do_robot import send_robot
from common.do_email import send_email
from case_api.login_password import LoginPassword


def create_suite():
    """创建测试套件"""
    case = unittest.TestLoader().discover(case_api_dir, pattern='*.py', top_level_dir=project_path)
    # case = unittest.TestLoader().loadTestsFromTestCase(LoginPassword)
    suite = unittest.TestSuite()
    suite.addTests(case)
    return suite


def unittest_beautiful():
    """使用BeautifulReport生成报告"""
    suite = create_suite()
    runner = BeautifulReport(suite)
    runner.report(filename=report_name, report_dir=report_dir, description='供应链金融接口自动化测试报告')


def send_report():
    """发送报告"""
    file_url = None
    if upload_MeterShpere or upload_robot or upload_email:
        file_url = get_file_url(report_name)
    if upload_MeterShpere:
        insert_report('cloud', report_name, file_url)
    if upload_robot:
        send_robot(file_url)
    if upload_email:
        send_email(file_url)


if __name__ == '__main__':
    unittest_beautiful()
    send_report()
