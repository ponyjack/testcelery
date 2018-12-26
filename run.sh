docker stop testcelery
docker rm testcelery
git pull
docker run  --name testcelery -v "$(pwd)":/home/testcelery  celery  celery -A lic.loadtask worker --loglevel=debug   -P gevent  --without-gossip --without-mingle --without-heartbeat --config=licconfig 
# docker run  -d  -v /home/testcelery:/home/testcelery  testcelery