# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pesantren_guru_quran(models.Model):
    _name = 'pesantren_guru_quran.pesantren_guru_quran'
    _description = 'pesantren_guru_quran.pesantren_guru_quran'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

