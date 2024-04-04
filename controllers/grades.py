from models.database import db
from models.grades import Grades
from sqlalchemy.sql import text


def set_grades(user, semesters):
    grades = db.session.query(Grades).filter_by(seq=user.seq).first()
    for semester in semesters.values():
        for course, grade in semester.items():
            setattr(grades, course, grade)
    db.session.commit()


def get_grades(user):
    return db.session.query(Grades).filter_by(seq=user.seq).first().__dict__


def get_rank(user):
    statement = """select t1.r from (select seq, row_number() over (order by
    total desc, seq asc) as r from grades where total > 0 and batch = :batch)
    t1 left join grades as t2 on t1.seq = t2.seq where t1.seq = :seq"""
    rank = db.session.execute(
        text(statement), {"seq": user.seq, "batch": user.batch}).first()[0]
    count = db.session.query(Grades).where(Grades.batch == user.batch,
                                           Grades.TOTAL > 0).count()
    return f"{rank}/{count}"
