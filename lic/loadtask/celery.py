from __future__ import absolute_import
from celery import Celery
import os

app = Celery(include=[ "lic.loadtask.slavetasks"])

if not app.conf.broker_url:
    app.conf.broker_url = os.getenv("broker_url")
    app.conf.result_backend = os.getenv("result_backend")
    if not app.conf.broker_url:
        if not app.config_from_envvar("LICCONFIG", silent=True):
            app.config_from_object("licconfig")
