from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

config = ConfigParser()
config.read('app_config/config_files/config.ini')
project_config = dict(config['projeto'])

engine = create_engine(project_config['dburl'])

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base = declarative_base()
