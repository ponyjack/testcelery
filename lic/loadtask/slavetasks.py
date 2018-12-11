from lic.loadtask.celery import app
import os
import gevent 
import time

def forLog(dursion):
    now  = time.time()
    while (time.time() - now<dursion):
        print "xxx"
        gevent.sleep(0)
        print "bbbb"


@app.task()
def StartSpaw(xxx):
    gevent.sleep(0)
    for _ in range(20):
        gevent.spawn(forLog, xxx)
    gevent.sleep(0)


