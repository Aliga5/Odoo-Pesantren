from odoo import models, fields

class AbsensiSiswa(models.Model):
    _name = 'tahun.pelajaran'
    _description = 'Data Tahun Pelajaran'

    name = fields.Char(string='Tahun Pelajaran', required=True)
    pembagian_termin = fields.Selection([
        ('1','Satu Semester'),
        ('2','Dua Semester'),
        ('3','Tiga Semester'),
        ('4','Empat Semester'),
        ('0','Other Semester'),
    ],string='Tahun Pelajaran')
    sart = fields.Date(string='Start Date')
    end = fields.Date(string='Start Date')
    keterangan = fields.Text(string='Keterangan')
    termin = fields.Char(string='Termin')
    biaya = fields.Char(string='Biaya')
    tagihan = fields.Char(string='Periode Tagihan')
