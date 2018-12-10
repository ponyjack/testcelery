FROM python:2
RUN pip install gevent
RUN pip install  celery psutil six redis 


RUN mkdir -p  /home/testcelery/


WORKDIR  /home/testcelery/
CMD celery -A lic.loadtask worker --loglevel=debug --config=licconfig 