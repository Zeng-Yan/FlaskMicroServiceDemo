## Overview

This demo is a Flask-based micoroservice offerring basic CURD operations via RESTful API.

## Project Structure

代码目录结构：

```
├─📄README.md             简介
├─📄.gitignore            Git忽略项配置
├─🐍unit_launcher.py      入口脚本
├─💼src                   代码模块
│  ├─🐍configs.py         配置项
│  ├─💼database           数据库模块
│  │  ├─🐍exts.py         数据库ORM对象声明与其他函数
│  │  └─🐍tables.py       数据表定义
│  └─💼funcs              功能函数模块
│     ├─🐍curd_views.py   增删查改相关的视图函数
│     └─🐍other_views.py  其他视图函数
└─📁docker                容器配置
   └─🐳Dockerfile         容器构建文件
```

## Quick Start 

run `unit_launcher.py` to start micoroservice.

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

build docker image. `cd` into `docker/` and run command:

```commandline
docker image build -t flask_microservice_demo .
```

save this image in `tar` format by running command:

```commandline
docker save -o zeng_falsk_ms.tar flask_microservice_demo:latest 
```

and load this image by running command:

```commandline
docker load -i zeng_falsk_ms.tar 
```

start micoroservice in a container by running command like:

```commandline
docker run -it \
    -v {...}/src:/home/src \
    -v {...}/unit_launcher.py:/home/unit_launcher.py \
    -p 9001:9001 \
    -u root \
    flask_microservice_demo:latest
```

run this command if using the outside dockerfile

```commandline
docker run -it -p 5000:9001 -u root flask_microservice_demo:latest
```
