# cython: language_level=3

import sys
import os


# Web configs
STATUS_CODE = {
    'success': 200,
    'error': 202
}

# MySQL Database configs
# HOST = '192.168.1.1'
# PORT = '6000'
# DATABASE = 'zeng'
# USERNAME = 'root'
# PASSWORD = '123456'
#
# DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8'

# SQLite Database configs
separator = '///' if sys.platform.startswith('win') else '////'  # 如果是 Windows 系统，使用三个斜线 否则使用四个斜线
DB_URI = f'sqlite:{separator}{os.getcwd()}/src/database/RDB.db'.replace('\\', '/')
print(DB_URI)

# Common Database configs
SQLALCHEMY_DATABASE_URI = DB_URI  # 设置连接数据库的URL
SQLALCHEMY_TRACK_MODIFICATIONS = True  # 设置sqlalchemy自动更跟踪数据库
SQLALCHEMY_ECHO = False  # 查询时不会显示原始SQL语句
SQLALCHEMY_COMMIT_ON_TEARDOWN = False  # 禁止自动提交数据处理

# WebSocket configs
# SOCKET_SECRET_KEY = 'heyjude'
# SOCKET_NAMESPACE = '/websocket'
# SOCKET_RECEIVER_NAME = 'client'
