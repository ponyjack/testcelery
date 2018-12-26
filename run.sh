docker stop testcelery
docker rm testcelery
git pull
docker run  --name testcelery -v "$(pwd)":/home/testcelery  testcelery  celery -A lic.loadtask worker --loglevel=debug  --loglevel=debug -P gevent -c 1  --without-gossip --without-mingle --without-heartbeat --config=licconfig 
# docker run  -d  -v /home/testcelery:/home/testcelery  testcelery