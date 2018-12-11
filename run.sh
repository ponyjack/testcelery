docker stop testcelery
docker rm testcelery
git pull
docker run  --name testcelery -v "$(pwd)":/home/testcelery  testcelery
# docker run  -d  -v /home/testcelery:/home/testcelery  testcelery