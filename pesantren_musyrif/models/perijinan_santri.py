from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.exceptions import ValidationError, UserError

class PerijinanSantri(models.Model):
    _name = 'perijinan.santri'
    _description = 'Ijin Santri'

    name = fields.Char(string="No Referensi (Auto)", readonly=True)
    tgl_ijin = fields.Date(string="Tanggal Ijin", default=fields.Date.today)
    siswa_id = fields.Char(string="Siswa", required=True)
    kelas = fields.Char(string="Kelas", readonly=True)
    kamar = fields.Char(string="Kamar", readonly=True)
    halaqoh = fields.Char(string="Halaqoh", readonly=True)
    musyrif = fields.Char(string="Musyrif", readonly=True)
    tgl_kembali = fields.Date(string="Tanggal Kembali", required=True)
    penjemput = fields.Char(string="Penjemput", required=True)
    lama_ijin = fields.Char(string="Lama Ijin", readonly=True)
    keperluan = fields.Text(string="Keperluan", required=True)
    catatan = fields.Text(string="Catatan")
    status_perijinan = fields.Selection([
		("pengajuan", "PENGAJUAN"),
		("diperiksa", "DIPERIKSA"),
		("disetujui", "DISETUJUI"),
        ("keluar", "IJIN KELUAR"),
        ("kembali", "KEMBALI"),
	], string="Status", default="pengajuan")
