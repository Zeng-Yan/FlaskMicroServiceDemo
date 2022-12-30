# cython: language_level=3

from flask import Flask

from src.database.exts import db
from src.configs import (
    SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS,
    SQLALCHEMY_COMMIT_ON_TEARDOWN, SQLALCHEMY_ECHO,
)

# 初始化
app = Flask(__name__)
# 微服务数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = SQLALCHEMY_COMMIT_ON_TEARDOWN
app.config['SQLALCHEMY_ECHO'] = SQLALCHEMY_ECHO


if __name__ == '__main__':
    from gevent import pywsgi

    with app.app_context():
        from src.funcs import curd_views, other_views
        from src.database import tables

        db.init_app(app)  # db绑定app
        db.create_all()  # 创建所有表
        # app.run(host='0.0.0.0', port=9001, debug=True)  # 启动服务
        server = pywsgi.WSGIServer(('0.0.0.0', 9001), app)
        server.serve_forever()
