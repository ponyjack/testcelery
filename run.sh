docker stop testcelery
docker rm testcelery
git pull
docker run  --name testcelery -v "$(pwd)":/home/testcelery --env broker_url=redis://10.11.65.34:6379/1 celery  celery -A lic.loadtask worker --loglevel=debug   -P gevent --without-gossip --without-mingle --without-heartbeat --config=licconfig
# docker run  -d  -v /home/testcelery:/home/testcelery  testcelery
# docker run  --name testcelery -v "$(pwd)":/home/testcelery --env CELERY_QUEUE=1111 celery




   




