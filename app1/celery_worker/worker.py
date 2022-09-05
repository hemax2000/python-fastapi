from app1.app.config import config
from commons.celery_worker.app import CustomTask, init_app

from .tasks.task1 import task1_

celery = init_app(config=config)


