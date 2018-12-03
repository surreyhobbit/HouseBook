# -*- coding: utf-8 -*-
# try something like
def index(): 
    worklist = db(db.Address).select()
    return locals()

@auth.requires_login()
def create():
    db.Address.Updated.default = request.now
    db.Address.Updated.writable=True
    db.Address.Updated.readable=True
    db.Address.Status.default = 'New'
    db.Address.Status.writable=False
    #db.Address.Status.readable=True
    form = SQLFORM(db.Address).process()
    if form.accepted:
        session.flash = "Entry created"
        redirect(URL('create'))
    return locals()

def show():
    entry=db.Address(request.args(0,cast=int))
    # default the foreign key for the blog post to the post ID being shown
    #db.blog_comment.blog_post.default = post.id
    #db.blog_comment.blog_post.readable=False
    #db.blog_comment.blog_post.writable=False
    #form = SQLFORM(db.blog_comment).process()
    #comments = db(db.blog_comment.blog_post==post.id).select()
    return locals()

def manage():
    grid = SQLFORM.grid(db.Address)
    return locals()
