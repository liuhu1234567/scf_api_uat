import requests
import json
from common.global_variable import customize_dict


def send_robot(file_url):
    """发送报告到企业微信机器人"""
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=8acebb19-c38e-4862-ab14-de3e3fda219f'
    headers = {'Content-Type': 'application/json'}
    testName = customize_dict['resultData']['testName']
    testAll = customize_dict['resultData']['testAll']
    testPass = customize_dict['resultData']['testPass']
    testFail = customize_dict['resultData']['testFail']
    beginTime = customize_dict['resultData']['beginTime']
    totalTime = customize_dict['resultData']['totalTime']
    testSkip = customize_dict['resultData']['testSkip']
    testError = customize_dict['resultData']['testError']
    md = f"""# {testName}


用例总数：{testAll}
    ├─ <font color="#dd0000">失败用例数：{testFail}</font>
    ├─ <font color="#228B22">通过用例数：{testPass}</font>
    ├─ <font color="#B8860B">跳过用例数：{testSkip}</font>
    └─ <font color="#B22222">报错用例数：{testError}</font>


运行时间：{totalTime}

查看 [详细报告]({file_url})"""
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": md
        }
    }
    data1 = {
        "msgtype": "text",
        "text": {
            "mentioned_mobile_list": ["@all"]
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"上传机器人结果：{r.text}")
    r1 = requests.post(url, headers=headers, data=json.dumps(data1))
    print(f"上传机器人结果：{r1.text}")
