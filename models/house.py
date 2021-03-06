# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

db.define_table('Person',
                Field('Name'),
                Field('Email'),
                format = '%name(s)')

db.define_table('OrderParty',
                Field('PartyName','string',requires=IS_NOT_EMPTY()),
                Field('AddrLine1','string'),
                Field('AddrLine2','string'),
                Field('AddrCity','string'),
                Field('PostCode','string'),
                Field('AddrCountry','string'),
                auth.signature)

db.define_table('Address',
                Field('Party','string',requires=IS_NOT_EMPTY()),
                Field('CustNo','string'),
                Field('Updated','date'),
                Field('Status','string'),
                Field('Comments','text'),
                Field('UKAddress','boolean'),
                Field('channel','string'),
                Field('Website','string'),
                Field('AppliesTo','string'),
                Field('PhoneNumber','string'),
                auth.signature)

db.define_table('Transactions',
                Field('TransDate','date'))

db.define_table('Jobs',
                Field('PartyId',db.OrderParty),
                Field('JobTitle','string'),
                Field('JobDate','date'),
                Field('Maintenance','boolean'),
                Field('Improvement','boolean'),
                Field('Comments','text'),
                Field('Updated','date'),
                Field('Status','string'),
                auth.signature
               )
