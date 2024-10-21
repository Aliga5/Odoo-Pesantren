from odoo import models, fields

class Provinsi(models.Model):
    _name = 'pesantren.provinsi'
    _description = 'Data Provinsi'

    name = fields.Char(string='Provinsi', required=True)
    negara = fields.Many2one('res.country', string='Negara', default=lambda self: self.env.ref('base.id').id)
    kota_id = fields.One2many('pesantren.kota', 'provinsi_id', string='Kota')


class Kota(models.Model):
    _name = 'pesantren.kota'
    _description = 'Data Kota'

    name = fields.Char(string='Kota', required=True)
    provinsi_id = fields.Many2one('pesantren.provinsi', string='Provinsi')
    kecamatan_id = fields.One2many('pesantren.kecamatan', 'kota_id', string='Kecamatan')


class Kecamatan(models.Model):
    _name = 'pesantren.kecamatan'
    _description = 'Data Kecamatan'

    name = fields.Char(string='Kecamatan', required=True)
    description = fields.Text(string='Deskripsi')
    kota_id = fields.Many2one('pesantren.kota', string='Kota')
