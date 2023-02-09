import sys
from datetime import datetime
from traceback import extract_stack

from laweb.enums import LogLevel
from laweb.tools import Formatter


class BaseLogger:
    def __init__(self) -> None:
        self.__formater = Formatter()

    def _log(self, msg: str, info: str | None, log_type: LogLevel):
        log = self.__formater.format(
            msg, datetime.now(), extract_stack()[-3], log_type
        )
        sys.stdout.write(log)

    def __check_msg(self):
        pass


class Logger(BaseLogger):
    def __init__(self) -> None:
        super().__init__()
        self.__out_only = True
        self.__host: str | None = None
        self.__port: str | None = None
        self.log_level: LogLevel | None = None

    def config(
        self, host: str | None, port: str | None, log_level: LogLevel = LogLevel.DEBUG
    ):
        self.log_level = log_level
        if host and port:
            self.__out_only = False

    def debug(self, msg: str, info: str | None = None):
        self._log(msg, info, LogLevel.DEBUG)

    def info(self, msg: str, info: str):
        pass

    def warning(self, msg: str, info: str):
        pass

    def error(self, msg: str, info: str):
        pass

    def critical(self, msg: str, info: str):
        pass
