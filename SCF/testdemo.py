import requests
import unittest
# from XTestRunner import HTMLTestRunner
from common.TestRunner import HTMLTestRunner

class YouTest(unittest.TestCase):


    def test_get(self):
        """测试get接口 """
        # r = requests.get("https://httpbin.org/get", params={"key":"value"})
        # print(r.json())
        # self.assertEqual(1+1,2)
        self.assertLessEqual(4, 3,'Test api timeout')

    def test_post(self):
        """测试post接口 """
        # r = requests.post("https://httpbin.org/post", data={"key":"value"})
        # print(r.json())
        self.assertEqual(1 + 1, 3)
        # self.assertLessEqual(4, 3, 'Test api timeout！')

    def test_put(self):
        """测试put接口 """
        # r = requests.put("https://httpbin.org/put", data={"key":"value"})
        # print(r.json())
        self.assertEqual(1 + 1, 2)
        raise Exception

    def test_pass(self):
        """测试put接口 """
        # r = requests.put("https://httpbin.org/put", data={"key":"value"})
        # print(r.json())
        self.assertEqual(1 + 1, 2)

    def test_pass2(self):
        """测试put接口 """
        # r = requests.put("https://httpbin.org/put", data={"key":"value"})
        # print(r.json())
        self.assertEqual(1 + 1, 2)

    @unittest.skip('  ')
    def test_delete(self):
        """测试delete接口 """
        # r = requests.delete("https://httpbin.org/delete", data={"key":"value"})
        # print(r.json())
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    # HTMLTestRunner
    report = "./result/api_result5.html"
    with(open(report, 'wb')) as fp:
        unittest.main(testRunner=HTMLTestRunner(
            stream=fp,
            language='zh-CN',
            title='供应链金融接口测试报告',
            description=['类型：API', '地址：http://app.scf-uat.dianliantech.com', '执行人：Crew']
        ))