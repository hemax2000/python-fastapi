from commons.main import set_up_main
from .api.auth.routes import auth_router,testhealth
from .config import config

app = set_up_main(
    config,
    routers_modules=[
        auth_router,
        testhealth
    ],
)
