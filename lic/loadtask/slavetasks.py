from lic.loadtask.celery import app, conf
import os
import gevent 


def forLog(dursion):
    now  = time.time()
    while (time.time() - now<dursion):
        print "xxx"
        gevent.sleep(0)

@app.task()
def StartSpaw(xxx):
    gevent.sleep(5)
    gevent.spawn(forLog, xxx)



