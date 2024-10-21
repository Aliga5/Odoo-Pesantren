from odoo import models, fields

class JamPelajaran(models.Model):
    _name = 'guru.jam_pelajaran'
    _description = 'Data Jam Pelajaran'

    name = fields.Char(string='Jam Pelajaran')