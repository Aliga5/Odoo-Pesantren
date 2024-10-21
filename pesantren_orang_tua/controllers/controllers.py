# -*- coding: utf-8 -*-
from odoo import http


class PesantrenOrangTua(http.Controller):
    @http.route('/pesantren_orang_tua/pesantren_orang_tua', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/pesantren_orang_tua/pesantren_orang_tua/objects', auth='public')
    def list(self, **kw):
        return http.request.render('pesantren_orang_tua.listing', {
            'root': '/pesantren_orang_tua/pesantren_orang_tua',
            'objects': http.request.env['pesantren_orang_tua.pesantren_orang_tua'].search([]),
        })

    @http.route('/pesantren_orang_tua/pesantren_orang_tua/objects/<model("pesantren_orang_tua.pesantren_orang_tua"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('pesantren_orang_tua.object', {
            'object': obj
        })

