# -*- coding: utf-8 -*-
# try something like
# def index(): return dict(message="hello from test.py")

response.menu = [['Register Party', False, URL('register_person')],
                 ['Plan Service', False, URL('plan_service')],
                 ['Buy service', False, URL('buy')],
                 ['Manage Orders', False, URL('manage_transactions')]
                ]

def register_person():
    # create an insert form from the table
    form = SQLFORM(db.person).process()

    # if form correct perform the insert
    if form.accepted:
        response.flash = 'new record inserted'

    # and get a list of all persons
    records = SQLTABLE(db().select(db.person.ALL),headers='fieldname:capitalize')

    return dict(form=form, records=records)

def plan_service():
    form = SQLFORM(db.service).process()
    if form.accepted:
        response.flash = 'new record inserted'
    records = SQLTABLE(db().select(db.service.ALL),
                       upload = URL('download'), # allows pics preview
                       headers='fieldname:capitalize')
    return dict(form=form, records=records)

def buy():
    form = SQLFORM.factory(
        Field('trader_id',requires=IS_IN_DB(db,db.person.id,'%(name)s')),
        Field('service_id',requires=IS_IN_DB(db,db.service.id,'%(name)s')),
        Field('amount','decimal(16,2)')).process()
    if form.accepted:
        # get previous purchese for same product
        purchase = db((db.purchase.trader_id == form.vars.trader_id)&
            (db.purchase.service_id==form.vars.service_id)).select().first()

        if purchase:
            # if list contains a record, update that record
            purchase.update_record(
                amount = purchase.amount+form.vars.amount)
        else:
            # self insert a new record in table
            db.purchase.insert(trader_id=form.vars.trader_id,
                               service_id=form.vars.service_id,
                               amount=form.vars.amount)
        response.flash = 'service purchased!'
    elif form.errors:
        response.flash = 'invalid values in form!'

    # now get a list of all purchases
    records = SQLTABLE(db(purchased).select(),headers='fieldname:capitalize')
    return dict(form=form, records=records)

def manage_transactions():
    grid = SQLFORM.smartgrid(db.person,linked_tables=['job','purchase'],
                             user_signature=False)
    return dict(grid=grid)

def download():
    return response.download(request,db)
