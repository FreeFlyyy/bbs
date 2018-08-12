# coding=utf-8

# 配置文件对象的属性名必须大写，否则无法导入

class __BaseConfig__:
    # 最大文件大小支持200M
    MAX_CONTENT_LENGTH = 200 * 1024 * 1024

class __DevConfig__(__BaseConfig__):
    DEBUG = True
    
class __OnlConfig(__BaseConfig__):
    DEBUG = False

dev = __DevConfig__()
onl = __OnlConfig()
