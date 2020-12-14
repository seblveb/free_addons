{
    'name': 'Invoice total due',
    'version': '13.0.1.0',
    'summery': 'Add total due to customer invoices',
    'description': '''
        Add total due to customer invoices
    ''',
    'author': 'Kareem Abuzaid, kareem.abuzaid123@gmail.com',
    'website': 'https://kareemabuzaid.com',
    'depends': [
        'account',
    ],
    'data': [
        'views/report_invoice.xml',
    ],
    'images': ['static/description/invoice.png'],
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
}
