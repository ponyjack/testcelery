from lic.loadtask.celery import app
import os
import gevent 
import time








@app.task()
def StartSpaw(xxx):
    print("Ddfsdfsdfsd")

    # gevent.sleep(0)
    # for _ in range(20):
    #     gevent.spawn(forLog, xxx)
    # gevent.sleep(0)
#     time.sleep(20)
#     forLog(xxx)


