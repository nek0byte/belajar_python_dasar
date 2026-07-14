"""
INNER CLASS (Nested Class)

Inner class adalah class yang didefinisikan di dalam class lain.
Berguna untuk mengelompokkan class yang saling terkait erat.
"""

"""
1. Inner class dasar
Class di dalam class, definisi dan cara akses.
Inner class bisa dibuat lewat outer class langsung.
"""


class Outer:
    class Inner:
        def info(self):
            return "ini Inner class"


obj = Outer.Inner()
print(obj.info())  # ini Inner class

"""
2. Inner class dengan objek outer
Inner class yang menyimpan referensi ke instance outer class-nya.
"""


class Mobil:
    def __init__(self, merk):
        self.merk = merk

    class Mesin:
        def __init__(self, outer_instance):
            self.outer = outer_instance

        def info(self):
            return f"Mesin mobil {self.outer.merk}"


m = Mobil("Toyota")
mesin = Mobil.Mesin(m)
print(mesin.info())  # Mesin mobil Toyota

"""
3. Membuat inner class lewat method outer (Factory method)
Outer class menyediakan method untuk membuat inner class-nya.
"""


class Komputer:
    def __init__(self, cpu_nama):
        self.cpu_nama = cpu_nama

    class CPU:
        def __init__(self, nama):
            self.nama = nama

        def info(self):
            return f"CPU: {self.nama}"

    def buat_cpu(self):
        return Komputer.CPU(self.cpu_nama)


k = Komputer("Intel i7")
cpu = k.buat_cpu()
print(cpu.info())  # CPU: Intel i7

"""
4. Multi-level inner class
Class di dalam class di dalam class (bersarang bertingkat).
"""


class Universitas:
    class Fakultas:
        class Jurusan:
            def __init__(self, nama):
                self.nama = nama

            def info(self):
                return f"Jurusan {self.nama}"


j = Universitas.Fakultas.Jurusan("Informatika")
print(j.info())  # Jurusan Informatika

"""
5. Private inner class (nama diawali _)
Inner class dengan _ atau __ tidak bisa diakses langsung dari luar.
"""


class ContohPrivate:
    class _Internal:
        def info(self):
            return "ini internal"

    def pakai_internal(self):
        i = self._Internal()
        return i.info()


c = ContohPrivate()
# print(ContohPrivate._Internal().info())  # bisa tapi tidak disarankan
print(c.pakai_internal())  # ini internal

"""
6. Inner class tanpa instance outer (static inner class)
Inner class yang tidak membutuhkan data dari outer class.
"""


class Kalkulator:
    class Operasi:
        @staticmethod
        def tambah(a, b):
            return a + b

        @staticmethod
        def kali(a, b):
            return a * b


print(Kalkulator.Operasi.tambah(3, 4))  # 7
print(Kalkulator.Operasi.kali(3, 4))  # 12

"""
7. Inner class mengakses atribut outer class lewat self
Inner class biasa yang menerima outer instance di __init__.
"""


class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    class GajiDetail:
        def __init__(self, karyawan):
            self.karyawan = karyawan

        def pajak(self, persen):
            return self.karyawan.gaji * persen / 100

        def info(self):
            return f"{self.karyawan.nama}: gaji Rp{self.karyawan.gaji:,}"


kar = Karyawan("Andi", 10_000_000)
gd = Karyawan.GajiDetail(kar)
print(gd.info())  # Andi: gaji Rp10,000,000
print(gd.pajak(10))  # 1000000.0

"""
8. Contoh real-world — Outer class menyembunyikan inner class
Inner class digunakan secara internal, tidak diekspos ke pengguna.
"""


class BankAccount:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self._riwayat = self._Transaksi()

    class _Transaksi:
        def __init__(self):
            self.daftar = []

        def tambah(self, tipe, jumlah):
            self.daftar.append({"tipe": tipe, "jumlah": jumlah})

        def semua(self):
            return self.daftar

    def simpan(self, jumlah):
        self._saldo = getattr(self, "_saldo", 0) + jumlah
        self._riwayat.tambah("simpan", jumlah)
        return self._saldo

    def tarik(self, jumlah):
        self._saldo = getattr(self, "_saldo", 0) - jumlah
        self._riwayat.tambah("tarik", jumlah)
        return self._saldo

    def cetak_riwayat(self):
        for t in self._riwayat.semua():
            print(f"  {t['tipe']}: Rp{t['jumlah']:,}")


b = BankAccount("Budi", 0)
b.simpan(5_000_000)
b.tarik(1_500_000)
print(f"Riwayat transaksi {b.pemilik}:")
b.cetak_riwayat()
# Riwayat transaksi Budi:
#   simpan: Rp5,000,000
#   tarik: Rp1,500,000

"""
9. __name__ == "__main__"
Kode demo di bawah hanya jalan saat file di-run langsung.
"""
if __name__ == "__main__":
    print("\nDemo inner class selesai.")
