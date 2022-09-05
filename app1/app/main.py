from commons.main import set_up_main

from .api.book.router import todo_router,testhealth
from .config import config

app = set_up_main(
    config,
    routers_modules=[
        todo_router,
        testhealth
    ],
)
