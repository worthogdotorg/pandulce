import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'llave-secreta-para-pandulce'
    SECRET_KEY = 'llave-secreta-para-pandulce'