from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Santri(models.Model):
    _name = 'pesantren.santri'
    _description = 'Data Santri Pesantren'

    name = fields.Char(string="Nama", required=True)
    foto = fields.Binary(string="Foto", required=True)  # Binary untuk menyimpan gambar
    city = fields.Char(string="Kota", required=True)
    birthdate = fields.Date(string="Tanggal Lahir", default=fields.Date.today, required=True)
    no_induk = fields.Char(string="Nomor Induk", copy=False, required=True)
    address = fields.Char(string="Alamat Rumah")
    provinsi_id = fields.Many2one('pesantren.provinsi', string="Provinsi")
    kota_id = fields.Many2one('pesantren.kota', string='Kota', domain="[('provinsi_id', '=', provinsi_id)]")
    kecamatan_id = fields.Many2one('pesantren.kecamatan', string='Kecamatan', domain="[('kota_id', '=', kota_id)]")

    jenis_partner = fields.Selection([
        ('siswa', 'Siswa'),
        ('orangtua', 'Orang Tua'),
        ('guru', 'Guru'),
        ('umum', 'Umum')
    ], string='Jenis Partner')
    rt_rw = fields.Char(string='RT / RW')

    wali_id = fields.Many2one('pesantren.wali_santri', string="Wali Santri", ondelete='cascade')
    phone = fields.Char(string="No. Telepon")
    email = fields.Char(string="Email")
    gender = fields.Selection([('male', 'Laki-laki'), ('female', 'Perempuan')], string="Jenis Kelamin", required=True)
    kelas_id = fields.Many2one('ruang.kelas', string='Kelas')
    kamar_id = fields.Many2one('pesantren.kamar', string='Kamar')
    pengurus_id = fields.Many2one('pesantren.pengurus', string='Pengurus')
    status_aktif = fields.Boolean(string='Status Aktif', default=True)
    siswa_ajaran = fields.Char(string='Siswa Ajaran')
    jenjang = fields.Char(string='Jenjang')
    bidang_jurusan = fields.Char(string='Bidang Jurusan')
    kamar = fields.Char(string='Kamar')
    musyrif_pembina = fields.Char(string='Musyrif Pembina')
    musyrif_pengganti = fields.Char(string='Musyrif Pengganti')
    nisn = fields.Char(string='NISN')
    ruang_kelas = fields.Char(string='Ruang Kelas')
    tingkat = fields.Char(string='Tingkat')
    kewarganegaraan = fields.Char(string='Kewarganegaraan')
    halaqoh = fields.Char(string='Halaqoh')
    penanggung_jawab = fields.Char(string='Penanggung Jawab')
    ustadz_pengganti = fields.Char(string='Ustadz Pengganti')
    nama_panggilan = fields.Char(string='Nama Panggilan')
    tanggal_lahir = fields.Char(string='Tanggal Lahir')
    jenis_kelamin = fields.Char(string='Jenis Kelamin')
    no_induk_keluarga = fields.Char(string='No Induk Keluarga')
    jml_saudara_kandung = fields.Char(string='Jml Saudara Kandung')
    hobi = fields.Char(string='Hobi')
    tempat_lahir = fields.Char(string='Tempat Lahir')
    golongan_darah = fields.Char(string='Golongan Darah')
    agama = fields.Char(string='Agama')
    anak_ke = fields.Char(string='Anak ke')
    bahasa_sehari_hari = fields.Char(string='Bahasa Sehari-hari')
    cita_cita = fields.Char(string='Cita-Cita')
    asal_sekolah = fields.Char(string='Asal Sekolah')
    nama_kepala_sekolah = fields.Char(string='Nama Kepala Sekolah')
    status_sekolah_asal = fields.Char(string='Status Sekolah Asal')
    no_telp_sekolah_asal = fields.Char(string='No Telp Sekolah Asal')
    alamat_sekolah_asal = fields.Char(string='Alamat Sekolah Asal')
    prestasi_diraih = fields.Char(string='Prestasi Diraih')
    bakat_siswa = fields.Char(string='Bakat Siswa')
    nilai_rata_rata_raport_kelas = fields.Char(string='Nilai Rata-Rata Raport Kelas')
    raport_4_sd_smt_1 = fields.Char(string='Raport 4 SD Smt 1')
    raport_5_sd_smt_1 = fields.Char(string='Raport 5 SD Smt 1')
    raport_4_sd_smt_2 = fields.Char(string='Raport 4 SD Smt 2')
    raport_5_sd_smt_2 = fields.Char(string='Raport 5 SD Smt 2')
    baca_quran = fields.Char(string='Baca Quran')
    virtual_account = fields.Char(string='Virtual Account')
    no_va_uang_saku = fields.Char(string='No. VA Uang Saku')

    @api.model
    def create(self, vals):
        if not vals.get('no_induk'):
            vals['no_induk'] = self.env['ir.sequence'].next_by_code('pesantren.santri') or '/'
        return super(Santri, self).create(vals)

    def write(self, vals):
        if not self.no_induk and not vals.get('no_induk'):
            vals['no_induk'] = self.env['ir.sequence'].next_by_code('pesantren.santri') or '/'
        return super(Santri, self).write(vals)

    @api.constrains('provinsi_id', 'wali_id')
    def check_mandatory_fields(self):
        if not self.provinsi_id or not self.wali_id:
            raise ValidationError("Provinsi dan Wali Santri harus diisi.")

    @api.model
    def kanban_button_action(self, additional_arg=None):
        return self.env.ref("pesantren.action_kanban_print").report_action(self)

class WaliSantri(models.Model):
    _name = 'pesantren.wali_santri'
    _description = 'Data Wali Santri'

    name = fields.Char(string="Nama Wali", required=True)
    relationship = fields.Selection([
        ('ayah', 'Ayah'),
        ('ibu', 'Ibu'),
        ('saudara', 'Saudara'),
        ('lainnya', 'Lainnya')
    ], string="Hubungan", required=True)
    phone = fields.Char(string="No. Telepon Wali", required=True)
    address = fields.Char(string="Alamat Wali", required=True)
    santri_ids = fields.One2many('pesantren.santri', 'wali_id', string="Santri yang Diasuh")

    def unlink(self):
        for record in self:
            record.santri_ids.unlink()
        return super(WaliSantri, self).unlink()
