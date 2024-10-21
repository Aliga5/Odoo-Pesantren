from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SiswaSearchWizard(models.TransientModel):
    _name = 'siswa.search.wizard'
    _description = 'Wizard Pencarian Siswa'

    no_induk = fields.Char(string='No Induk Siswa', required=True)
    siswa_id = fields.Many2one('pesantren.santri', string='Nama Siswa', readonly=True)
    tempat_lahir = fields.Char(string='Tempat Lahir', readonly=True)
    tgl_lahir = fields.Date(string='Tanggal Lahir', readonly=True)

    def action_search_siswa(self):
        """Aksi untuk tombol Search"""
        siswa = self.env['pesantren.santri'].search([('no_induk', '=', self.no_induk)], limit=1)
        if siswa:
            self.siswa_id = siswa.id
            self.tempat_lahir = siswa.tempat_lahir
            self.tgl_lahir = siswa.birthdate
        else:
            raise UserError(_("NIS '%s' tidak ditemukan. Silakan periksa kembali.") % self.no_induk)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'siswa.search.wizard',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
        }
