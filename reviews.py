from db import db
from sqlalchemy.sql import text

def avarage(restaurantnum):
    sql = text("SELECT ROUND(AVG(stars), 2) FROM " + restaurantnum + "")
    score = db.session.execute(sql).fetchone()
    return score[0]

def amount(restaurantnum):
    sql = text("SELECT COUNT(*) FROM " + restaurantnum + "")
    amount = db.session.execute(sql).fetchone()
    return amount[0]

def getreviews(restaurantnum):
    sql = text("SELECT id, username, review, stars, created_at FROM " + restaurantnum + " ORDER BY id DESC")
    result = db.session.execute(sql).fetchall()
    return result

def review(restaurantnum, username, review, stars):
    sql = text("INSERT INTO " + restaurantnum + " (username, review, stars, created_at) VALUES (:username, :review, :stars, NOW())")
    db.session.execute(sql, {"username":username, "review":review, "stars":stars})
    db.session.commit()


