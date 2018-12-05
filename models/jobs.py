# -*- coding: utf-8 -*-

db.define_table(
    'person',
    Field('name'),
    Field('email'),
    Field('phone'),
    format = '%(name)s')

# ONE (person) TO MANY (products)

db.define_table(
    'service',
    Field('trader_id',db.person),
    Field('name'),
    Field('description', 'text'),
    Field('maintenance', 'boolean'),
    Field('picture', 'upload', default=''),
    format = '%(name)s')

# MANY (persons) TO MANY (purchases)

db.define_table(
    'purchase',
    Field('trader_id', db.person),
    Field('service_id', db.service),
    Field('amount', 'decimal(16,2)'),
    format = '%(amount)s %(service_id)s -> %(trader_id)s')

purchased = (db.person.id==db.purchase.trader_id)&(db.service.id==db.purchase.service_id)

db.person.name.requires = IS_NOT_EMPTY()
db.person.email.requires = [IS_EMAIL(), IS_NOT_IN_DB(db, 'person.email')]
db.service.name.requires = IS_NOT_EMPTY()
#db.purchase.quantity.requires = IS_INT_IN_RANGE(0, 10)
