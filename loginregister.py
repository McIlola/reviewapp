from db import db
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

def user_id(username):
    sql = text("SELECT id FROM Users where username=:username")
    userid = db.session.execute(sql, {"username":username}).fetchone()
    return userid[0]

def checkuser(username):
    sql = text("SELECT id FROM Users where username=:username")
    user = db.session.execute(sql, {"username":username}).fetchone()
    if not user: return False
    return True

def getuser(username, password):
    sql = text("SELECT username, password FROM Users WHERE username=:username")
    user = db.session.execute(sql, {"username":username}).fetchone()
    if not user:
        return False
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            return True
        else:
            return False

def registeruser(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO Users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return getuser(username, password)
    