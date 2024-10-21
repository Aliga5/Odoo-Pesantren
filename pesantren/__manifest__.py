{
    'name': "Pesantren",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'license': 'LGPL-3',
    'description': """
    Long description of module's purpose
    """,
    'category': 'Management',
    'author': "UBIG",
    'version': '0.1',
    'depends': ['base', 'web', 'hr'],
    'data': [
        # Security CSV
        'security/ir.model.access.csv',
        
        # Kesantrian
        'views/kesantrian/pesantren_data_kesantrian.xml',
        'views/kesantrian/pesantren_kepesantrenan.xml',
        'views/kesantrian/pesantren_aktivitas.xml',
        'views/kesantrian/pesantren_pengaturan.xml',

        # Guru
        'views/guru/guru_aktivitas.xml',
        'views/guru/guru_pengaturan.xml',

        # Musyrif
        'views/musyrif/musyrif_perizinan.xml',
        'views/musyrif/musyrif_aktivitas.xml',
        'views/musyrif/musyrif_data_santri.xml',

        #Wali
        'views/wali/wali_kesantrian.xml',
        'views/wali/wali_akademik.xml',
        'views/wali/wali_aktifitas.xml',
        'views/wali/wali_keuangan.xml',
        'views/wali/wali_informasi.xml',

        # Guru Quran
        'views/guru_quran/guru_quran_kepesantrenan.xml',
        'views/guru_quran/guru_quran_data_santri.xml',

        # Petugas Keamanan
        'views/petugas_keamanan/petugas_keamanan_perizinan.xml',
        'views/petugas_keamanan/petugas_keamanan_keluar.xml',
        'views/petugas_keamanan/petugas_keamanan_masuk.xml',

        # Sekolah
        'views/sekolah/sekolah_siswa.xml',
        'views/sekolah/sekolah_guru.xml',
        'views/sekolah/sekolah_souce.xml',
        'views/sekolah/sekolah_aktivitas.xml',
        'views/sekolah/sekolah_pengaturan.xml',

        # Template
        'views/KTS.xml',

        #menu
        'views/pesantren_menu.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'assets': {
        'web.assets_backend': [
            'pesantren/static/src/css/style.css',
            # 'pesantren/static/src/xml/KTS.xml',
        ],
    }


}
