from db import db
from sqlalchemy.sql import text
import loginregister
from flask import session

def avarage(restaurantnum):
    sql = text("SELECT ROUND(AVG(stars), 2) FROM Reviews WHERE restaurant_id=:restaurant_id")
    score = db.session.execute(sql, {"restaurant_id": restaurantnum}).fetchone()
    return score[0]

def amount(restaurantnum):
    sql = text("SELECT COUNT(*) FROM Reviews WHERE restaurant_id=:restaurant_id")
    amount = db.session.execute(sql, {"restaurant_id": restaurantnum}).fetchone()
    return amount[0]

def getreviews(restaurantnum):
    sql = text("SELECT U.username, R.review, R.stars, R.created_at FROM Reviews R, Users U WHERE R.user_id=U.id AND restaurant_id=:restaurant_id ORDER BY R.id DESC")
    result = db.session.execute(sql, {"restaurant_id": restaurantnum}).fetchall()
    return result

def review(restaurant_id, review, stars):
    user_id = session["user_id"]
    sql = text("INSERT INTO Reviews (restaurant_id, user_id, review, stars, created_at) VALUES (:restaurant_id, :user_id, :review, :stars, NOW())")
    db.session.execute(sql, {"restaurant_id":restaurant_id, "user_id":user_id, "review":review, "stars":stars})
    db.session.commit()


