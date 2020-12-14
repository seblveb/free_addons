{
    'name': 'Base Airport',
    'version': '13.0.1.0',
    'summery': 'Add Airports data to odoo',
    'description': """
        Add Airports data to odoo
    """,
    'author': 'globalaircharter.com, Kareem Abuzaid',
    'website': 'https://globalaircharter.com',
    'depends': [
        'base',
        'mail',
    ],
    'images': ['static/description/airport_list.png'],
    'data': [
        'security/ir.model.access.csv',
        'data/res_airport_data.xml',
        'data/ir_cron_data.xml',
        'views/res_airport.xml',
    ],
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
}
