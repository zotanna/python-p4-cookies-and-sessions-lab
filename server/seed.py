#!/usr/bin/env python3

from random import randint

from faker import Faker

from app import app
from models import db, Article, User

db.init_app(app)

fake = Faker()

with app.app_context():

    Article.query.delete()
    User.query.delete()

    fake = Faker()

    users = [User(name=fake.name()) for i in range(25)]
    db.session.add_all(users)

    articles = []
    for i in range(100):
        content = fake.paragraph(nb_sentences=8)
        preview = content[:25]
        
        article = Article(
            author=fake.name(),
            title=fake.sentence(),
            content=content,
            preview=preview,
            minutes_to_read=randint(1,20),
        )

        articles.append(article)

    db.session.add_all(articles)
    
    db.session.commit()

