from db import db
from sqlalchemy.sql import text

def getuser(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username}).fetchone()
    if not result:
        return False
    return result

def registeruser(username, password):
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":password})
    db.session.commit()
    