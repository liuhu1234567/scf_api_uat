# -*- coding:UTF-8 -*-
import os
import git.cmd
from git.repo import Repo
import requests
import json
from common.do_config import git_url, git_msg_robot

class getFromGit():
    def is_dir(self, path):
        result = os.path.isdir(path + os.sep + ".git")
        if not result:
            print("路径:%s \n是否存在: %s" % (path, result))
            return result
        else:
            print("路径:%s \n是否存在: %s" % (path, result))
            return result

    def git_object(self, path):
        repo = Repo(path)
        git = repo.git
        remote = repo.remote()
        return repo, remote

    def reToRobot(self, url, REMOTE_URL, path):
        msg = self.git_clone(REMOTE_URL, path)
        branch_now, _ = self.git_branch_checkout(path)
        data = {
                "msgtype": "text",
                "text": {
                    "content": f"供应链金融{msg}代码分支{branch_now}。",
                    "mentioned_mobile_list": ["@all"]
                }
            }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, headers=headers, data=json.dumps(data))
        re = r.json()
        # print(re)

    def git_clone(self, remote_url, local_path):
        dir_msg = self.is_dir(local_path)
        # branch_now, repo = self.git_branch_checkout(local_path)
        if not dir_msg:
            Repo.clone_from(remote_url, to_path=local_path, branch='develop')
            msg = "代码已克隆到本地！"
            print(msg)
            return msg
        else:
            repo = Repo(local_path)
            repo.git.pull()
            msg = "本地代码已覆盖！"
            print(msg)
            return msg

    def git_branch_checkout(self, path):
        repo, remote = self.git_object(path)
        before = repo.git.branch()
        print(f'当前分支：{before}')
        if 'develop' not in before:
            repo.git.checkout('develop')
        now = repo.git.branch()
        return now, repo

if __name__ == '__main__':

    REMOTE_URL = git_url
    Robot_url = git_msg_robot
    dir_path = os.path.join("/root/auto_test", "SCF-test")
    s = getFromGit()
    s.reToRobot(Robot_url, REMOTE_URL, dir_path)
    # s.git_branch_checkout(dir_path)
    # s.git_clone(REMOTE_URL, dir_path)