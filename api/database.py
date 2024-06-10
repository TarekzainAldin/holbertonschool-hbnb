from .models import db, Country
import json

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        load_countries()

def load_countries():
    with open('countries.json') as f:
        countries = json.load(f)
        for country in countries:
            if not Country.query.filter_by(code=country['code']).first():
                db.session.add(Country(code=country['code'], name=country['name']))
        db.session.commit()
