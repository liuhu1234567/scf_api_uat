import requests
from common.do_config import api_host
from common.get_token import token_scf_platform
from config.all_path import report_dir
import os
from common.do_mysql import MyMysql
import time


def get_file_url(report_name):
    """获取文件url"""
    url = f'http://app.scf-uat.dianliantech.com/api-node/common/fileUpload'
    headers = {
        "x-appid-header": "1",
        "Authorization": token_scf_platform
    }
    path = os.path.join(report_dir, report_name)
    with open(path, 'rb') as f:
        file_b = f.read()
    files = {
        'uploadFile': (report_name, file_b)
    }
    r = requests.request("POST", url, headers=headers, files=files)
    fileId = r.json()['datas']['fileId']
    file_url = f"http://172.30.206.52:8100/{fileId}"
    return file_url


def insert_report(project, report_name, file_url):
    """上传报告到 metersphere"""
    projectid = {
        "电镀": "686f8fc7-8251-4650-8639-8a5da48ec154",
        "SCCP": "9f35bf7f-36ed-4fb6-8a73-f4d9fc6f70f1",
        "金点信": "73d44836-375a-4ffd-a817-b2e6a16bdace",
        "cloud": "d6ba9f42-6107-45a6-b209-c09f407939cb",
        "default": "f5c844d9-a4fa-11ec-a815-0242ac1e0a04"
    }
    project_id = projectid.get(project)
    report_code = str(time.time()).replace('.', '')
    db = MyMysql(
        host='172.30.206.57',
        user='root',
        password='Password123@mysql',
        port=3307,
        database='metersphere'
    )
    sql = F'''insert into metersphere.api_scenario_report(
            id,project_id,name,url_html,create_time,update_time,status,user_id,trigger_mode,execute_type,create_user,actuator,end_time,report_version,version_id,report_type)
            values (
            {report_code},"{project_id}","{report_name}","{file_url}",
            unix_timestamp(current_timestamp(3))*1000,unix_timestamp(current_timestamp(3))*1000,
            "Error","Crew","MANUAL","Saved","Crew","LOCAL",unix_timestamp(current_timestamp(3))*1000,2,
            "f2678995-0cf5-49b8-a23f-6380cf9d9c64","SCENARIO_INDEPENDENT")
        '''
    r = db.insert(sql)
    print(f'报告插入结果：{r}')
    db.close()
