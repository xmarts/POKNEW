# -*- coding: utf-8 -*-
{
    'name': "Product prr",

    'summary': """
        Agrega un nuevo campo para precio en el form del producto
        """,

    'description': """
        Agrega un nuevo campo para precio en el form del producto
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'stock', "quality_chemical_element"],

    # always loaded
    'data': [
	    'security/product_prr_security.xml',
        'security/ir.model.access.csv',
        "data/report_paperformat.xml",

        "views/product_view.xml",
        "views/product_menu_views.xml",

        "report/product_prr_report.xml",
    ],
}
