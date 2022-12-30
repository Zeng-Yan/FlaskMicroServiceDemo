## Overview

This demo is a Flask-based microservice offering basic CURD operations via RESTful API.

## Project Structure

```
├─📄README.md             简介
├─📄.gitignore            Git忽略项配置
├─🐚DockerDeploy.sh       简易CI镜像构建脚本    
├─🐍unit_launcher.py      入口脚本
├─💼src                   代码包
│  ├─🐍__init__.py        
│  ├─🐍configs.py         配置项
│  ├─💼database           数据库模块
|  │  ├─🐍__init__.py        
│  │  ├─🐍exts.py         ORM对象声明与其他类
│  │  └─🐍tables.py       数据表定义
│  └─💼funcs              功能函数模块
|     ├─🐍__init__.py        
│     ├─🐍curd_views.py   增删查改相关的视图函数
│     └─🐍other_views.py  其他视图函数
├─📁EnvDocker             运行环境镜像配置
│  └─🐳Dockerfile         镜像构建文件
└─📁DepDocker             服务部署镜像配置
   └─🐳Dockerfile         镜像构建文件
```

## Quick Start 

run `unit_launcher.py` to start microservice.

```commandline
python3 unit_launcher.py
```

visit the following URL in a local web browser to insert the first record into database.

```
localhost:9001/db/point/insert?latitude=23.4&longitude=123.4&altitude=234.5
```

visit the following URL in a local web browser to query all records of table `point` in database.

```
localhost:9001/db/point/query_all
```

## Deploy with Docker

Run `DockerDeploy.sh` to build Docker image automatically:

```commandline
. DockerDeploy.sh
```

After that two Docker images will be built and one of these will be packaged into a `.tar` file which can be loaded by running command:

```commandline
docker load -i zeng_db_op_ms.tar 
```

Then this microservice can be started in a container by running command like:

```commandline
docker run -it -p 9001:9001 -u root zeng_db_op_ms:latest
```

or 

```commandline
docker run -it \
    -v {...}/src:/home/src \
    -v {...}/unit_launcher.py:/home/unit_launcher.py \
    -p 9001:9001 \
    -u root \
    flask_sql_env:latest
```
