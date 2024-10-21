from odoo import models, fields

class MutabaahData(models.Model):
    _name='pesantren.mutabaah'
    _description = 'Data Mutabaah'

    name = fields.Char(string='Nama', required=True)
    kategory_ids = fields.Many2one('pesantren.mutabaah_kategory', string='Kategory')
    sesi_ids = fields.Many2one('pesantren.mutabaah_sesi', string='Sesi')
    active = fields.Boolean(string='Aktif', default=True)
    skor_nilai = fields.Integer(string='Skor Nilai')

class MutabaahData(models.Model):
    _name='pesantren.mutabaah_kategory'
    _description = 'Data Mutabaah'

    name = fields.Char(string='Nama', required=True)
    active = fields.Boolean(string='Aktif', default=True)
    
class MutabaahData(models.Model):
    _name='pesantren.mutabaah_sesi'
    _description = 'Data Mutabaah'

    name = fields.Char(string='Sesi Mutabaah', required=True)
    mulai = fields.Float(string='Jam Mulai', required=True)
    selesai = fields.Float(string='Jam Selesai', required=True)
    keterangan = fields.Text(string='Keterangan', required=True)
    active = fields.Boolean(string='Aktif', default=True)
    