from odoo import models, fields, api

class Pelanggaran(models.Model):
    _name = 'pesantren.pelanggaran'
    _description = 'Data Pelanggaran Santri'

    tanggal = fields.Date(string='Tanggal Pelanggaran', required=True)
    siswa_id = fields.Many2one('pesantren.santri', string='Nama Santri', required=True)
    kelas_id = fields.Many2one('ruang.kelas', string='Kelas', required=True)
    data_pelanggaran_id = fields.Many2one('pesantren.data.pelanggaran', string='Jenis Pelanggaran', required=True)
    kategori_id = fields.Many2one('pesantren.kategori.pelanggaran', string='Kategori Pelanggaran', required=True)
    poin = fields.Integer(string='Poin Pelanggaran', required=True)
    deskripsi = fields.Text(string='Deskripsi Pelanggaran')
    hukuman_ids = fields.Many2one('pesantren.hukuman', string='Hukuman')
    deskripsi_pelanggaran = fields.Text(string='Deskripsi Detail Pelanggaran')

    diperiksa_id = fields.Many2one('hr.employee', string='Diperiksa Oleh')
    catatan_ka_asrama_id = fields.Many2one('hr.employee', string='Catatan KA Asrama')
    tgl_disetujui = fields.Date(string='Tanggal Disetujui')
    usr_disetujui = fields.Many2one('hr.employee', string='Disetujui Oleh')

# Model untuk Data Pelanggaran
class DataPelanggaran(models.Model):
    _name = 'pesantren.data.pelanggaran'
    _description = 'Jenis Pelanggaran'

    name = fields.Char(string='Nama Pelanggaran', required=True)
    kategori_id = fields.Many2one('pesantren.kategori.pelanggaran', string='Kategori Pelanggaran')
    deskripsi = fields.Text(string='Deskripsi Pelanggaran')

# Model untuk Kategori Pelanggaran
class KategoriPelanggaran(models.Model):
    _name = 'pesantren.kategori.pelanggaran'
    _description = 'Kategori Pelanggaran'

    name = fields.Char(string='Kategori', required=True)
    poin_min = fields.Integer(string='Poin Minimum')
    poin_max = fields.Integer(string='Poin Maksimum')
    deskripsi = fields.Text(string='Deskripsi Kategori')

# Model untuk Hukuman
class Hukuman(models.Model):
    _name = 'pesantren.hukuman'
    _description = 'Data Hukuman'

    name = fields.Char(string='Nama Hukuman', required=True)
    poin_min = fields.Integer(string='Poin Minimum')
    poin_max = fields.Integer(string='Poin Maksimum')
    deskripsi = fields.Text(string='Deskripsi Hukuman')
