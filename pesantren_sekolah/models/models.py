# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pesantren_sekolah(models.Model):
    _name = 'pesantren_sekolah.pesantren_sekolah'
    _description = 'pesantren_sekolah.pesantren_sekolah'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

