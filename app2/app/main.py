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


"""def create_all_tables():
    # NOTE: this is not good at all ,, it is a temp work around so we don't do the migration set up now
    from sqlalchemy_utils import create_database, database_exists

    from app2.app.common.db import db
    from commons.db import Base

    if not database_exists(db.engine.url):
        create_database(db.engine.url)

    Base.metadata.drop_all(db.engine)"""
