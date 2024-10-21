from odoo import models, fields

class Hadist(models.Model):
    _name = 'tahfidz.hadist'
    _description = 'Data Hadist'

    name = fields.Char(string='Nama Hadist', required=True)
    kode = fields.Char(string='Kode Hadist', required=True)
    no_hadist = fields.Integer(string='Nomor Hadist', required=True)
    keterangan = fields.Text(string='Keterangan')
    mattan_hadist = fields.Text(string='Mattan Hadist', required=True)


class NilaiTahfidz(models.Model):
    _name = 'tahfidz.nilai'
    _description = 'Nilai Tahfidz'

    name = fields.Char(string='Nama', required=True)
    lulus = fields.Boolean(string='Lulus', default=False)


class SesiTahfidz(models.Model):
    _name = 'tahfidz.sesi'
    _description = 'Sesi Tahfidz'

    name = fields.Char(string='Nama Sesi', required=True)
    keterangan = fields.Text(string='Keterangan')


class BukuTahsin(models.Model):
    _name = 'buku.tahsin'
    _description = 'Buku Tahsin'

    name = fields.Char(string='Nama Buku', required=True)
    keterangan = fields.Text(string='Keterangan')