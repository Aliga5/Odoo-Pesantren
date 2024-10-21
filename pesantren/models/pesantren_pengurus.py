from odoo import models, fields

class Pengurus(models.Model):
    _name = 'pesantren.pengurus'
    _description = 'Data Pengurus'

    name = fields.Char(string='Nama Lengkap', required=True)
    nip = fields.Char(string='Nomor Induk Pengurus', required=True)
    jabatan = fields.Char(string='Jabatan', required=True)
    alamat = fields.Text(string='Alamat')
    no_telp = fields.Char(string='Nomor Telepon')
    is_active = fields.Boolean(string='Aktif', default=True)
    santri_ids = fields.One2many('pesantren.santri', 'pengurus_id', string='Santri yang Dibina')
