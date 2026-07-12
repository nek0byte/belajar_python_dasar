# class
class Person:
    def __init__(self, name, age):  # constructor = menginisialisasi objek
        self.name = name
        self.age = age


p1 = Person("John", 36)  # membuat objek

print(p1.name)
print(p1.age)


# class dengan method
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ini method
    def myfunc(self):  # 'self' digunakan untuk mengakses data milik objek
        print("Hello my name is " + self.name)


h1 = Human("John", 36)
h1.myfunc()


# ========================================
# Contoh Lain
class Waiter:
    def __init__(self, nama: str, umur: int, gaji: float) -> None:
        self.nama = nama
        self.umur = umur
        self.gaji = gaji
        self.pesanan_diantar: list[str] = []  # list kosong untuk menampung pesanan

    def ambil_pesanan(self, pesanan: str) -> None:
        # menambahkan pesanan ke pesanan_diantar
        print(f"Waiter {self.nama} mengambil pesanan, info pesanan: {pesanan}")

    def antar_pesanan(self, pesanan: str) -> None:
        # menambahkan pesanan ke pesanan_diantar
        self.pesanan_diantar.append(
            pesanan
        )  # menambahkan pesanan ke list pesanan_diantar
        print(f"Waiter {self.nama} menantikan pesanan, info pesanan: {pesanan}")
        self.cek_status()

    def cek_status(self) -> None:
        # cek jika waiter ready atau full
        if len(self.pesanan_diantar) > 5:
            self.status = "Full"
        else:
            self.status = "Ready"
        print(f"Waiter {self.nama} status: {self.status}")


# membuat objek
waiter_leon = Waiter("Leon", 23, 1_000_000)
waiter_vin = Waiter("Vin", 26, 2_000_000)

# memanggil method
print("================================")
waiter_leon.ambil_pesanan("Nasi Goreng")
waiter_leon.ambil_pesanan("Mie Goreng")

print("================================")
waiter_vin.ambil_pesanan("Bakso")
waiter_vin.ambil_pesanan("Es Teh")

print("================================")
waiter_leon.antar_pesanan("Nasi Goreng")
waiter_leon.antar_pesanan("Mie Goreng")

waiter_vin.antar_pesanan("Bakso")
waiter_vin.antar_pesanan("Es Teh")
print("================================")

# ========================================
# class atribute
from typing import Final  # Final = constant value (gak bisa diubah)


class Restoran:
    """
    class attribute = atribut/properti yang dimiliki oleh class
    kapan menggunakan attribute class? ketika data yg sama untuk semua instances
    """

    # class atribute
    nama_perusahaan: Final[str] = "Rattatouile"
    daftar_main_menu: Final[list[str]] = [
        "Nasi Goreng",
        "Mie Goreng",
        "Bakso",
        "Es Teh",
    ]  # daftar menu utama sama untuk setiap objek
    # menu menu utama disimpan ke dalam list

    # constructor
    def __init__(
        self,
        nama_cabang: str,
        alamat: str,
        jumlah_karyawan: int,
    ) -> None:

        # ini adalah instance atribute/atribut milik objek yg akan dibuat
        self.nama_cabang: str = nama_cabang
        self.alamat: str = alamat
        self.jumlah_karyawan: int = jumlah_karyawan
        self.income: float = 0.0
        self.menu_cabang: list[str] = Restoran.daftar_main_menu.copy()

    def ubah_menu_cabang(self, menu_baru: list[str]) -> None:
        self.menu_cabang = menu_baru
        print(
            f"Menu cabang {self.nama_cabang} telah diubah menjadi:\n {'\n'.join(menu_baru)}"
        )

    def info_restoran(self) -> None:
        print(f"Perusahaan:      {Restoran.nama_perusahaan}")
        print(f"Cabang:          {self.nama_cabang}")
        print(f"Alamat:          {self.alamat}")
        print(f"Menu:            {','.join(self.menu_cabang)}")
        print(f"Jumlah Karyawan: {self.jumlah_karyawan}")
        print(f"Income:          Rp.{self.income:.0f}")

    def resto_income(self, jumlah: float) -> None:
        self.income += jumlah


# membuat objek
resto_crab = Restoran("Crusty Crab", "Bikini Bottom", 2)
resto_chumb = Restoran("Chumb Bucket", "Bikini Bottom No. 2", 1)

resto_crab.info_restoran()
resto_crab.resto_income(100_000)
resto_crab.ubah_menu_cabang(["kraby patty", "fries", "soda"])
print()
resto_chumb.info_restoran()
resto_chumb.resto_income(200_000)
resto_chumb.ubah_menu_cabang(["chumb patty", "shitty fries", "tap water"])
print()

# ========================================
# class method
"""
class method adalah method yg ada di dalam class yg terikat pada class itu sendiri
bukan pada objek (instance) dari class

misal: 
"""
from datetime import datetime
from typing import Type


class Karyawan:
    # atribut global/class atribute
    perusahaan: Final[str] = "Citadel"
    tingkat_inflasi: Final[float] = 0.05
    semua_karyawan: list["Karyawan"] = []  # type hint
    # list["Karyawan"] maksudnya adalah s=list yg berisi objek bertipe Karyawan yg mengacu pada class Karyawan
    # jadi maksudnya seperti ini: [Karyawan(...), Karyawan(...), Karyawan(...)]
    # bukan: ["yami", "light"]
    # ditulis sebagai string karena saat basris itu dibaca, class Karyawan masih dalam proses didefinisikan

    def __init__(
        self, nama: str, posisi: str, gaji_bulan: float, tahun_masuk: int
    ) -> None:
        self.nama: str = nama
        self.posisi: str = posisi
        self.gaji_bulan: float = gaji_bulan
        self.tahun_masuk: int = tahun_masuk

        # memasukkan semua karyawan ke dalam list karyawan
        Karyawan.semua_karyawan.append(self)

    # misal kita ingin menampilkan info gaji tahunan
    """
    @classmethod adalah decorator untuk membuat class method 

    decorator adalah fitur untuk menambah atau mengubah perilaku fungsi
    tanpa mengubah kode asli fungsi

    'cls' digunakan untuk mengakses data milik class
    """

    @classmethod
    def dari_gaji_tahun(
        cls: Type["Karyawan"],
        nama: str,
        posisi: str,
        gaji_tahun: float,
        tahun_masuk: int,
    ) -> "Karyawan":
        gaji_bulan = gaji_tahun / 12
        return cls(nama, posisi, gaji_bulan, tahun_masuk)

    @classmethod
    def rata_gaji_karyawan(cls: Type["Karyawan"]) -> float:
        total_gaji = 0
        for karyawan in cls.semua_karyawan:
            total_gaji += karyawan.gaji_bulan
        return total_gaji / len(cls.semua_karyawan)

    def info_karyawan(self) -> None:
        lama_kerja = datetime.now().year - self.tahun_masuk
        print(f"Nama: {self.nama}")
        print(f"Posisi: {self.posisi}")
        print(f"Gaji: {self.gaji_bulan:.0f} / bulan")
        print(f"Lama Kerja: {lama_kerja} tahun")
        print(f"Perusahaan: {self.perusahaan}")


karyawan1 = Karyawan.dari_gaji_tahun("Yami", "Designer", 120_000_000, 2020)
karyawan2 = Karyawan.dari_gaji_tahun("Light", "Project Manager", 150_000_000, 2018)

print("===============================")

print("===============================")
karyawan1.info_karyawan()
print("===============================")
karyawan2.info_karyawan()
print("===============================")

# ========================================
# static method
"""
static method adalah method di dalam class
yang tidak membutuhkan akses ke objek (self) maupun class (cls).
"""


class RekeningBank:
    bunga_tahunan = 0.05

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo

    def tampilkan_saldo(self):
        print(f"Pemilik: {self.pemilik}")
        print(f"Saldo: Rp {self.saldo:,.0f}")

    @staticmethod
    def validasi_saldo(saldo):
        """
        Mengecek apakah saldo awal valid
        """
        return saldo >= 0

    @staticmethod
    def format_rupiah(angka):
        """
        Mengubah angka menjadi format Rupiah
        """
        return f"Rp {angka:,.0f}".replace(",", ".")

    @staticmethod
    def hitung_bunga(saldo, lama_tahun):
        """
        Menghitung bunga berdasarkan saldo dan lama waktu
        """
        bunga = saldo * 0.05 * lama_tahun
        return bunga


saldo_awal = 10_000_000

if RekeningBank.validasi_saldo(saldo_awal):
    rekening1 = RekeningBank("Yami", saldo_awal)

    print("\n===========================================")
    rekening1.tampilkan_saldo()

    bunga = RekeningBank.hitung_bunga(rekening1.saldo, 3)

    print("Bunga 3 tahun:", RekeningBank.format_rupiah(bunga))
print("===========================================")
