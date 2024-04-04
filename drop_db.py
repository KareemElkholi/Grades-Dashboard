#!/usr/bin/python3
from sqlalchemy import create_engine
from utilities.env import DB_URI
from sqlalchemy_utils import database_exists, drop_database

engine = create_engine(DB_URI)

if database_exists(engine.url):
    drop_database(engine.url)
