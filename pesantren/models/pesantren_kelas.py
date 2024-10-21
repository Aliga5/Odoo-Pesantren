from odoo import models, fields, api

class Kelas(models.Model):
    _name = 'pesantren.asset'
    _description = 'Data Kelas'

    name = fields.Char(string='Nama Kelas', required=True)
    tingkatan = fields.Selection([('1', 'Tingkat 1'), ('2', 'Tingkat 2'), ('3', 'Tingkat 3')], string='Tingkatan', required=True)
    guru_id = fields.Many2one('pesantren.guru', string='Wali Kelas')
    santri_ids = fields.One2many('pesantren.santri', 'kelas_id', string='Daftar Santri')
class RuangKelas(models.Model):
    _name = 'ruang.kelas'
    _description = 'Data Ruang Kelas'

    name = fields.Char(string='Ruang Kelas', required=True)
    jenjang = fields.Selection([('sd', 'SD/MI'), ('smp', 'SMP/MTS'), ('sma', 'SMA/MA')], string='Jenjang', required=True)
    tingkatan = fields.Char(string='Tingkat', required=True)
    guru_id = fields.Many2one('pesantren.guru', string='Wali Kelas')
    keterangan = fields.Char(string='Keterangan')
    santri_ids = fields.One2many('pesantren.santri', 'kelas_id', string='Daftar Siswa')
    jumlah_siswa = fields.Integer(string='Jumlah Siswa', compute='_compute_count_siswa')

    @api.depends('santri_ids')
    def _compute_count_siswa(self):
        for record in self:
            record.jumlah_siswa = len(record.santri_ids)
