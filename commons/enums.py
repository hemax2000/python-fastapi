"""
common enums used in multiple apps
"""

from enum import Enum


class AppName(str, Enum):
    APP1 = "app1"
    APP2 = "app2"


class LoggingLevel(str, Enum):
    CRITICAL = "CRITICAL"
    FATAL = "FATAL"
    ERROR = "ERROR"
    WARN = "WARN"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    NOTSET = "NOTSET"
