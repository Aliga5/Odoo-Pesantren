from odoo import models, fields

class AbsensiSiswa(models.Model):
    _name = 'guru.absensi_siswa'
    _description = 'Data Absensi Siswa'

    tanggal = fields.Date(string="Tanggal")
    kelas_id = fields.Many2one('guru.kelas', string="Kelas")
    hari = fields.Selection([
        ('senin', 'Senin'),
        ('selasa', 'Selasa'),
        ('rabu', 'Rabu'),
        ('kamis', 'Kamis'),
        ('jumat', 'Jumat'),
        ('sabtu', 'Sabtu'),
        ('minggu', 'Minggu')
    ], string="Hari")
    jam_ke = fields.Integer(string="Jam Ke")
    mata_pelajaran_id = fields.Many2one('guru.mata_pelajaran', string="Mata Pelajaran")
    guru_id = fields.Many2one('guru.guru', string="Guru")
    siswa_id = fields.Many2one('pesantren.siswa', string='Siswa')
    nis = fields.Char(string='NIS')
    kehadiran = fields.Selection([
        ('hadir', 'Hadir'),
        ('sakit', 'Sakit'),
        ('izin', 'Izin'),
        ('alpa', 'Alpa')
    ], string="Kehadiran")
    pertemuan_ke = fields.Integer(string="Pertemuan Ke")
    tema = fields.Char(string="Tema")
    materi = fields.Char(string="Materi")
    rpp = fields.Char(string="RPP")
