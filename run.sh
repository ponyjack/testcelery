docker stop testcelery
docker rm testcelery
git pull
docker run  --name testcelery -v "$(pwd)":/home/testcelery --env CELERY_QUEUE=1111 celery  celery -A lic.loadtask worker --loglevel=debug   -P gevent -c 1  --without-gossip --without-mingle --without-heartbeat --config=licconfig
# docker run  -d  -v /home/testcelery:/home/testcelery  testcelery
# docker run  --name testcelery -v "$(pwd)":/home/testcelery --env CELERY_QUEUE=1111 celery




   




