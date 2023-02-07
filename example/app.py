from test import test

from flask import Flask

from laweb import logger

app = Flask(__name__)
logger.config("127.0.0.1", 8000)

app.add_url_rule("/", view_func=test)
