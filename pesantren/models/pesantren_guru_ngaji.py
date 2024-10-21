from odoo import models, fields

class Guru(models.Model):
    _name = 'pesantren.guru_ngaji'
    _description = 'Data Guru'

    name = fields.Char(string='Nama Lengkap', required=True)
    nip = fields.Char(string='Nomor Induk Guru', required=True)
    mata_pelajaran = fields.Char(string='Mata Pelajaran', required=True)
    alamat = fields.Text(string='Alamat')
    no_telp = fields.Char(string='Nomor Telepon')
    is_active = fields.Boolean(string='Aktif', default=True)
