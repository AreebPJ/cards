import random
from application import app, db
from application.models import deck

@app.route('/')
def reset():
    if str(deck.query.all()) != '[]':
        db.session.query(deck).delete()
        db.session.commit()
    suits = ["Hearts","Spades","Clubs","Diamonds"]
    cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    for suit in suits:
        value = 1
        for card in cards:
            value += 1
            carddata = deck(card = card, suit = suit, value = value)
            db.session.add(carddata)
            db.session.commit()
    return" TEST"            
