cd EnvDocker
docker image build -t flask_sql_env .
cd ..
mv DepDocker/Dockerfile Dockerfile
docker image build -t zeng_db_op_ms .
docker save -o zeng_db_op_ms.tar zeng_db_op_ms:latest
mv Dockerfile DepDocker/Dockerfile
