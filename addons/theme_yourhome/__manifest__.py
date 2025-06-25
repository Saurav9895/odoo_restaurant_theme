{
    'name': 'YourHome Theme',
    'description': 'YourHome website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/header.xml',
        'views/footer.xml',
        'views/homepage.xml',
        'views/services_page.xml',
        'views/menus.xml',
        'views/order_page.xml',
        'views/order_detail.xml',
        'views/products_page.xml',
        'views/category-product.xml',
        'views/my-account.xml',
        'views/snippets/property-agents.xml',
        'views/snippets/new-properties.xml',
        'views/snippets/product-snippets.xml',
        'views/snippets/product-tab.xml',
        'views/snippets/benefits.xml',
        'views/snippets/banner.xml',
        'views/snippets/categories.xml',
        'views/snippets/testimonial.xml',
        'views/snippets/about-us.xml',
        'views/snippets/our-story.xml',
        'views/snippets/snippets.xml',
        'views/snippets/mycat.xml',
        # 'views/snippets/rent_mega_menu.xml',
        # 'views/snippets/explore-cities.xml',
        
        # 'views/yh_cities.xml',
    ],
    'assets':{
        'web.assets_frontend': [
          
          ('include', 'website.assets_frontend'),
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',
            

            'theme_yourhome/static/src/scss/styles.scss',
            'theme_yourhome/static/src/scss/property-agents.scss',
            'theme_yourhome/static/src/js/explore-cities.js',
            'theme_yourhome/static/src/js/explore-cities-options.js',
           

        ],
        'web._assets_primary_variables': [
            "theme_yourhome/static/src/scss/primary_variables.scss",
        ]
    },
    'images': [
    ],
    'snippet_lists': {
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
