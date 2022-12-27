FROM python:3.7.15-slim
COPY src /home/src/
COPY unit_launcher.py /home/unit_launcher.py
EXPOSE 9001
WORKDIR /home
RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install Flask-SQLAlchemy -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install gevent -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD python3 unit_launcher.py
# docker run -it -p 5000:9001 -u root flask_microservice_demo:latest
