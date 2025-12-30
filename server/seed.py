#!/usr/bin/env python3

from app import app
from models import db, Bakery, BakedGood

with app.app_context():

    BakedGood.query.delete()
    Bakery.query.delete()

    # Create bakeries
    delightful_donuts = Bakery(name="Delightful donuts")
    incredible_crullers = Bakery(name="Incredible crullers")
    
    db.session.add_all([delightful_donuts, incredible_crullers])
    db.session.commit()

    # Create baked goods
    baked_goods = [
        BakedGood(name="Chocolate dipped donut", price=2.75, bakery=delightful_donuts),
        BakedGood(name="Apple-spice filled donut", price=3.50, bakery=delightful_donuts),
        BakedGood(name="Glazed honey cruller", price=3.25, bakery=incredible_crullers),
        BakedGood(name="Chocolate cruller", price=3.40, bakery=incredible_crullers)
    ]
    
    db.session.add_all(baked_goods)
    db.session.commit()
