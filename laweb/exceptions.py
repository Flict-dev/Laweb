class BaseException(Exception):
    """
    Base Exception.
    """


class LongMsgError(BaseException):
    """
    The LongMsgError is raised when msg field too long (msg > 500 symb)
    """


class EmptyMsgError(BaseException):
    """
    The EmptyMsgError is raised when msg is empty
    """


class ConfigurationError(BaseException):
    """
    The ConfigurationError is raised when there is a problem in configuration
    """
