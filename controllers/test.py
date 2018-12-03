# -*- coding: utf-8 -*-
# try something like
# def index(): return dict(message="hello from test.py")

response.menu = [['Register Party', False, URL('register_person')],
                 ['Register Product', False, URL('register_product')],
                 ['Buy product', False, URL('buy')]]

def register_person():
    # create an insert form from the table
    form = SQLFORM(db.party).process()

    # if form correct perform the insert
    if form.accepted:
        response.flash = 'new record inserted'

    # and get a list of all persons
    records = SQLTABLE(db().select(db.party.ALL),headers='fieldname:capitalize')

    return dict(form=form, records=records)

def register_product():
    form = SQLFORM(db.job).process()
    if form.accepted:
        response.flash = 'new record inserted'
    records = SQLTABLE(db().select(db.product.ALL),
                       upload = URL('download'), # allows pics preview
                       headers='fieldname:capitalize')
    return dict(form=form, records=records)

def buy():
    form = SQLFORM.factory(
        Field('party_id',requires=IS_IN_DB(db,db.person.id,'%(name)s')),
        Field('job_id',requires=IS_IN_DB(db,db.product.id,'%(name)s')),
        Field('amount','decimal(16,2)')).process()
    if form.accepted:
        # get previous purchese for same product
        purchase = db((db.purchase.party_id == form.vars.buyer_id)&
            (db.purchase.job_id==form.vars.job_id)).select().first()

        if purchase:
            # if list contains a record, update that record
            purchase.update_record(
                amount = purchase.amount+form.vars.quantity)
        else:
            # self insert a new record in table
            db.purchase.insert(party_id=form.vars.party_id,
                               job_id=form.vars.job_id,
                               amount=form.vars.amount)
        response.flash = 'product purchased!'
    elif form.errors:
        response.flash = 'invalid values in form!'

    # now get a list of all purchases
    records = SQLTABLE(db(purchased).select(),headers='fieldname:capitalize')
    return dict(form=form, records=records)

def manage_transactions():
    grid = SQLFORM.smartgrid(db.party,linked_tables=['job','purchase'],
                             user_signature=False)
    return dict(grid=grid)

def download():
    return response.download(request,db)