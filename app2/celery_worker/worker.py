from app2.app.config import config
from app2.celery_worker.tasks.task1 import task1_
from commons.celery_worker.app import CustomTask, init_app

celery = init_app(config=config)


@celery.task(max_retries = 3)
def task1(email: str):
    task1_(email)
