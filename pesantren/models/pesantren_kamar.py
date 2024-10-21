from odoo import models, fields

class Kamar(models.Model):
    _name = 'pesantren.kamar'
    _description = 'Data Kamar'

    name = fields.Char(string='Nama Kamar', required=True)
    kapasitas = fields.Integer(string='Kapasitas', required=True)
    santri_ids = fields.One2many('pesantren.santri', 'kamar_id', string='Daftar Santri')
    pengurus_id = fields.Many2one('pesantren.pengurus', string='Pengurus Kamar')
