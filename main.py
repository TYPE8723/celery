from celery import Celery
CELERY_BACKEND_REDIS = 'redis://127.0.0.1:6379/3'
CELERY_BROKER_URL_REDIS = 'redis://127.0.0.1:6379/4'
# add celery task locations here
CELERY_TASKS = ['tasks']

# **SETUP NOTES**
# set a redis backend,broker db to keep log of each api . ex-> redis://127.0.0.1:6379/3
#
# add tasks in CELERY_TASKS with the location of files where tasks are defined OR celery_app.autodiscover_tasks() to register celery tasks
# for normal celery consumer exceution -> celery --app=apps.devbudcore.utils.celery:celery_app worker -l info
# for development consumer execution -> celery --app=apps.devbudcore.utils.celery:celery_app worker -l debug
celery_app = Celery(
    __name__,
    backend=CELERY_BACKEND_REDIS,
    BROKER_URL=CELERY_BROKER_URL_REDIS,
    include=CELERY_TASKS,#once the tasks are added and the celery task begins execution,all the tasks mentioned in CELERY_TASKS get initialized
)


# add celery task locations here
# celery_app.autodiscover_tasks(
#     [
#         "apps.mailer.mailer",
#         "apps.sast.crud.shared_connected_providers",
#         "apps.devbudcore.utils.utils",
#     ],
#     force=True,
# )
