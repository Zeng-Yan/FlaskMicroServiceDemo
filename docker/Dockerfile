FROM python:3.7.15-slim
EXPOSE 9001
WORKDIR /home
RUN pip install flask && \
    pip install pymysql && \
    pip install Flask-SQLAlchemy && \
    pip install gevent
CMD python3 unit_launcher.py
