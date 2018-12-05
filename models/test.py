# -*- coding: utf-8 -*-

#db.define_table(
#    'person',
#    Field('name'),
#    Field('email'),
#    format = '%(name)s')


# ONE (person) TO MANY (products)

db.define_table(
    'product',
    Field('seller_id',db.person),
    Field('name'),
    Field('description', 'text'),
    Field('picture', 'upload', default=''),
    format = '%(name)s')

# MANY (persons) TO MANY (purchases)

#db.define_table(
#    'purchase',
#    Field('buyer_id', db.person),
#    Field('product_id', db.product),
#    Field('quantity', 'integer'),
#    format = '%(quantity)s %(product_id)s -> %(buyer_id)s')

#purchased = (db.person.id==db.purchase.buyer_id)&(db.product.id==db.purchase.product_id)

#db.person.name.requires = IS_NOT_EMPTY()
#db.person.email.requires = [IS_EMAIL(), IS_NOT_IN_DB(db, 'person.email')]
#db.product.name.requires = IS_NOT_EMPTY()
#db.purchase.quantity.requires = IS_INT_IN_RANGE(0, 10)
