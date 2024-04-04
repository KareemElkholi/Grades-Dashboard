#!/usr/bin/python3
from sqlalchemy import create_engine
from utilities.env import DB_URI
from sqlalchemy_utils import database_exists, create_database
from models.database import Base
from models.users import Users
from models.grades import Grades
from sqlalchemy.orm import Session
from json import load
from sys import argv

engine = create_engine(DB_URI)

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)

with Session(engine) as session:
    if not session.query(Users).filter_by(batch=argv[1]).first():
        with open(f"{argv[1]}.json", "r") as file:
            users = load(file)
        for user in users:
            session.add(Users(id=user["id"], name=user["name"], batch=argv[1]))
            session.add(Grades(batch=argv[1]))
        session.commit()
