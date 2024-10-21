# -*- coding: utf-8 -*-
from odoo import http


class PesantrenMusyrif(http.Controller):
    @http.route('/pesantren_musyrif/pesantren_musyrif', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/pesantren_musyrif/pesantren_musyrif/objects', auth='public')
    def list(self, **kw):
        return http.request.render('pesantren_musyrif.listing', {
            'root': '/pesantren_musyrif/pesantren_musyrif',
            'objects': http.request.env['pesantren_musyrif.pesantren_musyrif'].search([]),
        })

    @http.route('/pesantren_musyrif/pesantren_musyrif/objects/<model("pesantren_musyrif.pesantren_musyrif"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('pesantren_musyrif.object', {
            'object': obj
        })

