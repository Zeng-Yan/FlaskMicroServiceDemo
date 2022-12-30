cd EnvDocker
docker image build -t flask_sql_env .
cd ..
mv DepDocker/Dockerfile Dockerfile
docker image build -t p105_db_op_ms .
docker save -o p105_db_op_ms.tar p105_db_op_ms:latest
mv Dockerfile DepDocker/Dockerfile
