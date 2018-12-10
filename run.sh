docker rm testcelery
git pull
docker run  --name testcelery -v "$(pwd)":/home/testcelery testcelery