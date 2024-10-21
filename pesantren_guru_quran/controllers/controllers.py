# -*- coding: utf-8 -*-
from odoo import http


class PesantrenGuruQuran(http.Controller):
    @http.route('/pesantren_guru_quran/pesantren_guru_quran', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/pesantren_guru_quran/pesantren_guru_quran/objects', auth='public')
    def list(self, **kw):
        return http.request.render('pesantren_guru_quran.listing', {
            'root': '/pesantren_guru_quran/pesantren_guru_quran',
            'objects': http.request.env['pesantren_guru_quran.pesantren_guru_quran'].search([]),
        })

    @http.route('/pesantren_guru_quran/pesantren_guru_quran/objects/<model("pesantren_guru_quran.pesantren_guru_quran"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('pesantren_guru_quran.object', {
            'object': obj
        })

