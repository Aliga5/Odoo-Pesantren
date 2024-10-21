from odoo import models, fields

class Guru(models.Model):
    _name = 'pesantren.guru'
    _description = 'Data Guru'

    name = fields.Char(string='Nama Lengkap', required=True)
    nip = fields.Char(string='Nomor Induk Guru', required=True)
    mata_pelajaran = fields.Char(string='Mata Pelajaran', required=True)
    alamat = fields.Text(string='Alamat')
    no_telp = fields.Char(string='Nomor Telepon')
    is_active = fields.Boolean(string='Aktif', default=True)
    kelas_ids = fields.Many2many('ruang.kelas', string='Kelas yang Diajar')

class GuruAbsensi(models.Model):
    _name = 'guru.absen_siswa'
    _description = 'Absensi Siswa Oleh guru'

    tanggal = fields.Date(string="Tanggal", required=True)
    kelas = fields.Many2one(string='')