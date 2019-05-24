## 实现通过Web页面实时查看日志
### 技术组件
- bottle
- websocket
- subprocess

### 示例
```bash
# 启动服务端
python wss-server.py

# 启动日志收集器
python wss-collect.py

# 指定文件写入数据
for n in {1..100};do echo "test: $n" >>/tmp/wss-test.log && sleep 1;done 

# 浏览器打开页面查看显示效果
file:///E:/github/wss-log/wss-test.html
```