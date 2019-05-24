#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time     : 2019-05-24 14:38
# @Author   : yang.hong
# @FILE     : wss-server.py
# @Software : PyCharm

from bottle import get, run
from bottle_websocket import websocket, GeventWebSocketServer

# 连接进来的websocket客户端集合
users = set()


@get('/websocket/', apply=[websocket])
def chat(ws):
    users.add(ws)
    while True:
        msg = ws.receive()
        if msg:
            for u in users:
                u.send(msg)
        else:
            break
    users.remove(ws)


run(host='0.0.0.0', port=8000, server=GeventWebSocketServer)
