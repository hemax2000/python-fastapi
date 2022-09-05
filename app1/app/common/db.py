from importlib import import_module
from app1.app.config import config
from commons.db import BaseDb, Base

db = BaseDb(config)
