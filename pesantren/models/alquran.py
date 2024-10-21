from odoo import models, fields

class Surah(models.Model):
    _name = 'alquran.surah'
    _description = 'Data Surah'

    name = fields.Char(string='Nama Surah (Arab)', required=True)
    surah_id = fields.Integer(string='Nomor Surah', required=True)
    arti = fields.Char(string='Arti Surah', required=True)
    jumlah_ayat = fields.Integer(string='Jumlah Ayat', required=True)
    tempat_turun = fields.Selection([
        ('mekah', 'Mekah'),
        ('madinah', 'Madinah')
    ], string='Tempat Turun', required=True)
    ayat_ids = fields.Many2many('alquran.ayat', string='Ayat')


class Ayat(models.Model):
    _name = 'alquran.ayat'
    _description = 'Data Ayat'

    number = fields.Integer(string='Ayat Ke', required=True)
    juz = fields.Integer(string='Juz', required=True)
    manzil = fields.Integer(string='Manzil', required=True)
    ruku = fields.Integer(string='Ruku', required=True)
    hizb = fields.Integer(string='Hizb', required=True)
    halaman = fields.Integer(string='Halaman', required=True)
