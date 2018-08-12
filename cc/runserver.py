# coding=utf-8

import center
import configure

# 传入配置文件创建app
app = center.create_app(configure.dev)

#app.run(host='0.0.0.0')
app.run()