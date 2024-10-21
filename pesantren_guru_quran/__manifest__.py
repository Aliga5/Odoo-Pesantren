# -*- coding: utf-8 -*-
{
    'name': "PesantrenGuruQuran",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "UBIG",
    'category': 'Uncategorized',
    'version': '0.1',
    'application':True,

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/absensi_tahfidz_tahsin.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

