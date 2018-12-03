# -*- coding: utf-8 -*-

db.define_table(
    'party',
    Field('name'),
    Field('email'),
    format = '%(name)s')

db.define_table(
    'job_category',
    Field('category'),
    Field('description', 'text'),
    format = '%(category)s')

# ONE (category) TO MANY (jobs)

db.define_table(
    'job',
    Field('category_id',db.job_category),
    Field('name'),
    Field('description', 'text'),
    Field('picture', 'upload', default=''),
    format = '%(name)s')

# MANY (partys) TO MANY (jobs)

db.define_table(
    'purchase',
    Field('party_id', db.party),
    Field('job_id', db.job),
    Field('job_date','date'),
    Field('amount', 'decimal(16,2)'),
    format = '%(amounts)s %(job_id)s -> %(party_id)s')

purchased = (db.party.id==db.purchase.party_id)&(db.job.id==db.purchase.job_id)

db.party.name.requires = IS_NOT_EMPTY()
db.party.email.requires = [IS_EMAIL(), IS_NOT_IN_DB(db, 'party.email')]
db.job.name.requires = IS_NOT_EMPTY()
# db.purchase.amount.requires = IS_INT_IN_RANGE(0, 10)
