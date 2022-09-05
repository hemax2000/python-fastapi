from commons.config import (
    CommonBaseConfig,
    CommonProductionConfig,
    CommonStagingConfig,
    CommonTestingConfig,
    current_config,
)


class BaseConfig(CommonBaseConfig):
    APP_NAME: str = "app1"


class ProductionConfig(CommonProductionConfig, BaseConfig):  # type: ignore
    pass


class StagingConfig(CommonStagingConfig, BaseConfig):  # type: ignore
    pass


class TestingConfig(CommonTestingConfig, BaseConfig):  # type: ignore
    pass


config: BaseConfig = current_config(ProductionConfig, StagingConfig, TestingConfig, BaseConfig)
