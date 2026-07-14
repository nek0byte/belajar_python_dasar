from typing import Optional


class Aset:
    def __init__(self, kode: str, nama: str, harga: int) -> None:
        self.kode = kode
        self.nama = nama
        self.harga = harga


class AsetKendaraan(Aset):
    def __init__(self, kode: str, nama: str, harga: int, stkn: str, tahun: int) -> None:
        super().__init__(kode, nama, harga)
        self.stkn = stkn
        self.tahun = tahun


class AsetElektronik(Aset):
    def __init__(self, kode: str, nama: str, harga: int, serial_number: str) -> None:
        super().__init__(kode, nama, harga)
        self.serial_number = serial_number


class AsetTanahBangunan(Aset):
    def __init__(self, kode: str, nama: str, harga: int, sertifikat: str, njop: int, luas: int) -> None:
        super().__init__(kode, nama, harga)
        self.sertifikat = sertifikat
        self.njop = njop
        self.luas = luas


class DaftarAset:
    def __init__(self) -> None:
        self.daftar_aset: list[Aset] = []

    def tambah_aset(self, aset: Aset) -> None:
        self.daftar_aset.append(aset)

    def ambil_aset(self, kode: str) -> Optional[Aset]:
        for aset in self.daftar_aset:
            if aset.kode == kode:
                return aset
        return None

    def hapus_aset(self, kode: str) -> bool:
        for i, aset in enumerate(self.daftar_aset):
            if aset.kode == kode:
                del self.daftar_aset[i]
                return True
        return False
