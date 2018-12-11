from lic.loadtask.celery import app
import os
import gevent 
import time

def forLog(dursion):
    now  = time.time()
    while (time.time() - now<dursion):
        print "xxx"
        gevent.sleep(0)

@app.task()
def StartSpaw(xxx):
    gevent.sleep(5)
    gevent.spawn(forLog, xxx)



