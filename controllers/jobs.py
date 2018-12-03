# -*- coding: utf-8 -*-
# try something like
def index(): 
    worklist = db(db.Jobs).select()
    return locals()

def create():
    db.Jobs.Updated.default = request.now
    db.Jobs.Updated.writable=True
    db.Jobs.Updated.readable=True
    db.Jobs.Status.default = 'New'
    db.Jobs.Status.writable=False
    #db.Jobs.Status.readable=True
    form = SQLFORM(db.Jobs).process()
    if form.accepted:
        session.flash = "Entry created"
        redirect(URL('create'))
    return locals()

def manage():
    grid = SQLFORM.grid(db.Jobs)
    return locals()
