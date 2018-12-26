docker stop testcelery
docker rm testcelery
git pull
docker run  --name testcelery -v "$(pwd)":/home/testcelery --env CELERY_QUEUE=1111 celery  
# docker run  -d  -v /home/testcelery:/home/testcelery  testcelery