#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time     : 2019-05-24 15:10
# @Author   : yang.hong
# @FILE     : wss-collect.py
# @Software : PyCharm

import subprocess
from websocket import create_connection

ws_server = 'ws://192.168.22.163:8000/websocket/'
cmd = '/usr/bin/tailf {log_path}'.format(log_path='/tmp/wss-test.log')


def collect_log():
    """获取远程服务器实时日志，并发送到websocket服务端"""
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print('连接成功')
    ws = create_connection(ws_server)
    while True:
        line = popen.stdout.readline().strip()
        if line:
            ws.send(line)


if __name__ == '__main__':
    collect_log()
