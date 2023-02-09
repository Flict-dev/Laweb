import logging

from laweb import logger


def test():
    logger.debug("Test")
    return f"<p>{logger.__class__.__dict__}</p>"
