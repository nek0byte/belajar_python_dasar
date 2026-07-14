from models import (
    AsetKendaraan,
    AsetElektronik,
    AsetTanahBangunan,
    DaftarAset,
)

import views


class AsetController:
    def __init__(self) -> None:
        self.daftar_aset = DaftarAset()

    def run(self) -> None:
        while True:
            views.tampilkan_menu_utama()
            pilih = views.input_int_opsi("Pilih menu: ", 1, 3)

            if pilih == 1:
                self.tambah_aset()
            elif pilih == 2:
                self.lihat_aset()
            elif pilih == 3:
                break

    def tambah_aset(self) -> None:
        while True:
            views.tampilkan_menu_tambah()
            pilih = views.input_int_opsi("Pilih menu: ", 1, 4)

            if pilih == 1:
                data = views.input_aset_kendaraan()
                aset = AsetKendaraan(*data)
                self.daftar_aset.tambah_aset(aset)
                views.tampilkan_pesan("Kendaraan berhasil ditambahkan")

            elif pilih == 2:
                data = views.input_aset_elektronik()
                aset = AsetElektronik(*data)
                self.daftar_aset.tambah_aset(aset)
                views.tampilkan_pesan("Elektronik berhasil ditambahkan")

            elif pilih == 3:
                data = views.input_aset_tanah_bangunan()
                aset = AsetTanahBangunan(*data)
                self.daftar_aset.tambah_aset(aset)
                views.tampilkan_pesan("Tanah Bangunan berhasil ditambahkan")

            elif pilih == 4:
                break

    def lihat_aset(self) -> None:
        if not self.daftar_aset.daftar_aset:
            views.tampilkan_pesan("Belum ada aset.")
            return

        for aset in self.daftar_aset.daftar_aset:
            if isinstance(aset, AsetKendaraan):
                views.tampilkan_aset_kendaraan(aset)
            elif isinstance(aset, AsetElektronik):
                views.tampilkan_aset_elektronik(aset)
            elif isinstance(aset, AsetTanahBangunan):
                views.tampilkan_aset_tanah_bangunan(aset)

        views.tampilkan_menu_setelah_lihat()
        pilih = views.input_int_opsi("Pilih menu: ", 1, 3)

        if pilih == 1:
            self.ubah_aset()
        elif pilih == 2:
            self.hapus_aset()

    def ubah_aset(self) -> None:
        kode = views.input_kode()
        aset = self.daftar_aset.ambil_aset(kode)

        if aset is None:
            views.tampilkan_pesan(f"Tidak ditemukan aset dengan kode: {kode}")
            return

        if isinstance(aset, AsetKendaraan):
            nama, harga, stkn, tahun = views.input_data_ubah_kendaraan()
            aset.nama = nama
            aset.harga = harga
            aset.stkn = stkn
            aset.tahun = tahun

        elif isinstance(aset, AsetElektronik):
            nama, harga, serial_number = views.input_data_ubah_elektronik()
            aset.nama = nama
            aset.harga = harga
            aset.serial_number = serial_number

        elif isinstance(aset, AsetTanahBangunan):
            nama, harga, sertifikat, njop, luas = views.input_data_ubah_tanah_bangunan()
            aset.nama = nama
            aset.harga = harga
            aset.sertifikat = sertifikat
            aset.njop = njop
            aset.luas = luas

        views.tampilkan_pesan("Aset berhasil diubah")

    def hapus_aset(self) -> None:
        kode = views.input_kode()
        if self.daftar_aset.hapus_aset(kode):
            views.tampilkan_pesan("Aset berhasil dihapus")
        else:
            views.tampilkan_pesan(f"Tidak ditemukan aset dengan kode: {kode}")
