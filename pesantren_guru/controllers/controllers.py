# -*- coding: utf-8 -*-
# from odoo import http


# class PesantrenGuru(http.Controller):
#     @http.route('/pesantren_guru/pesantren_guru', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pesantren_guru/pesantren_guru/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pesantren_guru.listing', {
#             'root': '/pesantren_guru/pesantren_guru',
#             'objects': http.request.env['pesantren_guru.pesantren_guru'].search([]),
#         })

#     @http.route('/pesantren_guru/pesantren_guru/objects/<model("pesantren_guru.pesantren_guru"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pesantren_guru.object', {
#             'object': obj
#         })

