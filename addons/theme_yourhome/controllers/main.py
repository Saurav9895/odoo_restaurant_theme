from odoo import http
from odoo.http import request


class ThemeYourHome(http.Controller):

    @http.route('/products', type='http', auth='public', website=True)
    def products(self, **kwargs):
        """Display all product categories and products."""
        categories = request.env['product.public.category'].search([])
        products = request.env['product.template'].sudo().search([
            ('website_published', '=', True)
        ])
        return request.render('theme_yourhome.products_page', {
            'categories': categories,
            'products': products,
            'category': None,  # No active category on /products
        })

    @http.route('/products/category/<int:category_id>', type='http', auth='public', website=True)
    def category_products(self, category_id, **kwargs):
        """Display products for a specific category including subcategories."""
        categories = request.env['product.public.category'].search([])
        category = request.env['product.public.category'].sudo().browse(category_id)

        if not category.exists():
            return request.not_found()

        products = request.env['product.template'].sudo().search([
            ('public_categ_ids', 'child_of', category.id),
            ('website_published', '=', True)
        ])

        return request.render('theme_yourhome.category_product_page', {
            'categories': categories,
            'category': category,
            'products': products,
        })

    @http.route('/orders', type='http', auth='user', website=True)
    def orders(self, **kwargs):
        """Display only orders placed by the logged-in user."""
        user_partner = request.env.user.partner_id
        orders = request.env['sale.order'].search([
            ('partner_id', '=', user_partner.id),
            ('state', 'in', ['sale', 'done'])
        ], order="date_order desc")

        return request.render('theme_yourhome.order_page', {
            'orders': orders,
        })

    @http.route('/orders/<int:order_id>', type='http', auth='user', website=True)
    def order_detail(self, order_id, **kwargs):
        """Display details of a specific order, only if it belongs to the logged-in user."""
        order = request.env['sale.order'].sudo().browse(order_id)
        user_partner = request.env.user.partner_id

        if not order.exists() or order.partner_id.id != user_partner.id:
            return request.not_found()

        return request.render('theme_yourhome.order_detail_page', {
            'order': order,
            'order_lines': order.order_line,
        })

    @http.route('/account', type='http', auth='user', website=True)
    def my_account(self, **kwargs):
        """Display My Account page for the logged-in user."""
        user = request.env.user
        partner = user.partner_id

        return request.render('theme_yourhome.my_account_page', {
            'user': user,
            'partner': partner,
        })
