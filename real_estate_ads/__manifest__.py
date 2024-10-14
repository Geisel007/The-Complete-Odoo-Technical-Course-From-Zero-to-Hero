{
    "name": "Real Estate Ads",
    "version": "1.0",
    "website": "htttps//www.theodoobd.com",
    "author": "gmsolano",
    "description": """
        Real Estate module to show available properties
    """,
    "category": "",
    "depends": ["base", "mail", "website"],
    "data": [
        # Groups
        'security/ir.model.access.csv',
        'security/res_group.xml',
        #'security/model_access.xml',
        #'security/ir_rule.xml',

        #View
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/property_offer_view.xml',
        'views/menu_items.xml',
        'views/property_web_template.xml',

        # Data Files
        #'data/property_type.xml'
        'data/estate.property.type.csv',
        'data/mail_template.xml',

        # Report
        'report/report_template.xml',
        'report/property_report.xml'
    ],
    "demo": [
        'demo/property_tag.xml'
    ],
    "assets": {
      'web.assets_backend': [
          'real_estate_ads/static/src/js/my_custom_tag.js',
          'real_estate_ads/static/src/xml/my_custom_tag.xml',
      ]
    },
    "installable": True,
    "aplication": True,
    "license": "LGPL-3"
}