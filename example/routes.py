from laweb import logger


def test():
    logger.log("Test")
    return f"<p>{logger.__class__.__dict__}</p>"
