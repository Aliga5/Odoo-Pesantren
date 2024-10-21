# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pesantren_musyrif(models.Model):
    _name = 'pesantren_musyrif.pesantren_musyrif'
    _description = 'pesantren_musyrif.pesantren_musyrif'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

