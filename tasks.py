from main import celery_app
import time

#celery tasks can be defined like the bellow funtion with a celery app decorator
@celery_app.task()
def test_task(n):
    delay = n
    print("task started \n delayed for",n)
    time.sleep(delay)
    print(f"task completed in {delay} seconds")
