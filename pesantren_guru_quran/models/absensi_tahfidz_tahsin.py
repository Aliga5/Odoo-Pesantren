from odoo import models, fields

class AbsensiSiswaTahfidz(models.Model):
    _name = 'guru.absensi_tahfidz'
    _description = 'Data Absensi Siswa Tahfidz'

    tanggal = fields.Date(string="Tanggal")
    sesi_id = fields.Many2one('absensi_tahfidz.sesi', string='Sesi')
    halaqoh = fields.Char(string='Halaqoh')
    keterangan = fields.Text(string='Keterangan')
    tahun_ajaran_id = fields.Many2one('tahun.pelajaran', string='Tahun Ajaran')
    guru_id = fields.Many2one('hr.employee', string="Guru")
    siswa_id = fields.Many2one('pesantren.santri', string='Siswa')
    nis = fields.Char(string='NIS')
    kehadiran = fields.Selection([
        ('hadir', 'Hadir'),
        ('sakit', 'Sakit'),
        ('izin', 'Izin'),
        ('alpa', 'Alpa')
    ], string="Kehadiran")
    
    status = fields.Selection([
        ('draf', 'Draf'),
        ('proses', 'Proses'),
        ('selesai', 'Selesai')
    ], string="Status", default='draf')


class AbsensiSiswaTahsin(models.Model):
    _name = 'guru.absensi_tahsin'
    _description = 'Data Absensi Siswa Tahsin'

    tanggal = fields.Date(string="Tanggal")
    halaqoh = fields.Char(string='Halaqoh')
    tahun_ajaran_id = fields.Many2one('tahun.pelajaran', string='Tahun Ajaran')
    guru_id = fields.Many2one('hr.employee', string="Guru")
    siswa_id = fields.Many2one('pesantren.santri', string='Siswa')
    nis = fields.Char(string='NIS')
    kehadiran = fields.Selection([
        ('hadir', 'Hadir'),
        ('sakit', 'Sakit'),
        ('izin', 'Izin'),
        ('alpa', 'Alpa')
    ], string="Kehadiran")
    
    status = fields.Selection([
        ('draf', 'Draf'),
        ('proses', 'Proses'),
        ('selesai', 'Selesai')
    ], string="Status", default='draf')


class AbsenSesiTahfidz(models.Model):
    _name = 'absensi_tahfidz.sesi'
    _description = 'Data Sesi Tahfidz'

    name = fields.Char(string='Nama Sesi', required=True)
    keterangan = fields.Text(string='Keterangan')

# class InheritPesantrenSantri(models.Model):
#     _inherit = 'pesantren.santri'

#     absen_tahfidz_list = fields.One2many('guru.absensi_tahfidz',string='Absen Tahfidz')
#     absen_tahsin_list = fields.One2many('guru.absensi_tahsin',string='Absen Tahsin')