# -*- coding: utf-8 -*-
# from odoo import http


# class PesantrenSekolah(http.Controller):
#     @http.route('/pesantren_sekolah/pesantren_sekolah', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pesantren_sekolah/pesantren_sekolah/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pesantren_sekolah.listing', {
#             'root': '/pesantren_sekolah/pesantren_sekolah',
#             'objects': http.request.env['pesantren_sekolah.pesantren_sekolah'].search([]),
#         })

#     @http.route('/pesantren_sekolah/pesantren_sekolah/objects/<model("pesantren_sekolah.pesantren_sekolah"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pesantren_sekolah.object', {
#             'object': obj
#         })

