from odoo import http
from odoo.http import request


class ThemeYourHome(http.Controller):

    @http.route('/products', type='http', auth='public', website=True)
    def products(self, **kwargs):
        """Display all product categories."""
        categories = request.env['product.public.category'].search([])
        return request.render('theme_yourhome.products_page', {
            'categories': categories,
        })

    @http.route('/orders', type='http', auth='user', website=True)
    def orders(self, **kwargs):
        """Display only orders placed by the logged-in user."""
        user_partner = request.env.user.partner_id

        orders = request.env['sale.order'].search([
            ('partner_id', '=', user_partner.id),
            ('state', 'in', ['sale', 'done'])  # optionally show only confirmed/done orders
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
            'order_lines': order.order_line
        })
