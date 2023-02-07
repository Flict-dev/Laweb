import traceback
from datetime import datetime

from laweb.enums import LogLevel


class BaseLogger:
    def __log(self, msg: str, info, log_type):
        traceback.extract_stack()
        datetime.now()
        # format msg by using log type with formater

    def __check_msg(self):
        pass


class Logger(BaseLogger):
    def __init__(self) -> None:
        self.__out_only = True
        self.__host: str | None = None
        self.__port: str | None = None
        self.log_level = LogLevel.DEBUG

    def config(self, host: str | None, port: str | None, log_level: LogLevel):
        if host and port:
            self.__out_only = False

    def debug(self, msg: str, info: str):
        pass

    def info(self, msg: str, info: str):
        pass

    def warning(self, msg: str, info: str):
        pass

    def error(self, msg: str, info: str):
        pass

    def critical(self, msg: str, info: str):
        pass
