# coding=utf-8

from flask import Flask
import functools

def create_app(config):
    if config != None:
        pass

    # 设置默认以utf-8形式打开文件
    global open
    open = functools.partial(open, encoding='utf-8')

    # 创建服务器
    app = Flask(__name__)

    # 导入配置文件对象
    app.config.from_object(config)

    return app