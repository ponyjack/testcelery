BROKER_URL = 'redis://10.11.65.34:6379/1'
CELERY_RESULT_BACKEND = 'redis://10.11.65.34:6379/2'

# CELERYD_MAX_TASKS_PER_CHILD=1

CELERYD_CONCURRENCY=1