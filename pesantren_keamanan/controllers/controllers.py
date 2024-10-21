# -*- coding: utf-8 -*-
# from odoo import http


# class PesantrenKeamanan(http.Controller):
#     @http.route('/pesantren_keamanan/pesantren_keamanan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pesantren_keamanan/pesantren_keamanan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pesantren_keamanan.listing', {
#             'root': '/pesantren_keamanan/pesantren_keamanan',
#             'objects': http.request.env['pesantren_keamanan.pesantren_keamanan'].search([]),
#         })

#     @http.route('/pesantren_keamanan/pesantren_keamanan/objects/<model("pesantren_keamanan.pesantren_keamanan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pesantren_keamanan.object', {
#             'object': obj
#         })

