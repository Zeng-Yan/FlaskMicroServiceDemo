FROM flask_sql_env:latest
COPY src /home/src/
COPY unit_launcher.py /home/unit_launcher.py
EXPOSE 9001
WORKDIR /home
CMD python3 unit_launcher.py
