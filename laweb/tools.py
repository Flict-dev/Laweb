from datetime import datetime
from traceback import FrameSummary

from enums import Colors, LogLevel


class Formatter:
    def format(
        self, msg: str, created_at: datetime, file_from: FrameSummary, log_type: LogLevel
    ) -> str:
        """OKCYAN = "\033[52m"
        print()
        r = "\033[1m"
        print(f"{OKCYAN}{r}[{log_type.value}]: {created_at} - {msg}
        """
