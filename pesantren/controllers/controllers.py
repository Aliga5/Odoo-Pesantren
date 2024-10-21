# -*- coding: utf-8 -*-
from odoo import http


class Pesantren(http.Controller):
    @http.route('/pesantren/pesantren', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/pesantren/pesantren/objects', auth='public')
    def list(self, **kw):
        return http.request.render('pesantren.listing', {
            'root': '/pesantren/pesantren',
            'objects': http.request.env['pesantren.pesantren'].search([]),
        })

    @http.route('/pesantren/pesantren/objects/<model("pesantren.pesantren"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('pesantren.object', {
            'object': obj
        })

