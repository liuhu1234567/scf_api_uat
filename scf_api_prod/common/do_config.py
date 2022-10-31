from config.all_path import get_config_path
import json
from string import Template
import time


def read_config():
    """读取config.json文件"""
    with open(get_config_path('config.json'), 'r', encoding='utf-8') as config_f:
        config = json.load(config_f)
    return config


start_time = time.strftime('%Y%m%d_%H-%M-%S')
_config = read_config()
restime = _config['restime']
env_now = _config['env_now']
environment = _config['environment']
test_type = _config['test_type']
api_host = _config['all_host'][env_now]
report_name = Template(_config['report_name']).safe_substitute(start_time=start_time)
scf_financier = _config['scf_financier']
scf_enterprise = _config['scf_enterprise']
scf_supplier = _config['scf_supplier']
scf_platform = _config['scf_platform']
scf_factor = _config['scf_factor']
scf_subsidiaries = _config['scf_subsidiaries']
upload_MeterShpere = _config['upload_report']['upload_MeterShpere']
upload_robot = _config['upload_report']['upload_robot']
upload_email = _config['upload_report']['upload_email']
host = _config['all_host']['prod']
git_url = _config['git_url']
git_msg_robot = _config['git_msg_robot']