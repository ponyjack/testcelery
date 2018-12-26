docker stop testcelery
docker rm testcelery
git pull
docker run  --name testcelery -v "$(pwd)":/home/testcelery  testcelery  celery -A lic.loadtask worker --loglevel=debug  --config=licconfig -c 1
# docker run  -d  -v /home/testcelery:/home/testcelery  testcelery