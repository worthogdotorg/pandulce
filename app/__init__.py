from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from logging.handlers import RotatingFileHandler
import logging
import os

#-- app = Flask(__name__, template_folder="templates") 
# def create_app(config_class=Config):
app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)

#if not app.debug:
# 
#    if not os.path.exists('logs'):
#        os.mkdir('logs')
#    file_handler = RotatingFileHandler('logs/bread.log', maxBytes=10240,
#                                       backupCount=10)
#    file_handler.setFormatter(logging.Formatter(
#        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
#    file_handler.setLevel(logging.INFO)
#    app.logger.addHandler(file_handler)
#
#    app.logger.setLevel(logging.INFO)
#    app.logger.info('Bread startup')


from app import routes