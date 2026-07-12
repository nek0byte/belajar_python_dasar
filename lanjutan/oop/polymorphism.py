# Polymorphism (banyak bentuk)
"""
satu interface tapi banyak implementasi,
- memungkinkan bisa memanggil sebuah method yg sama pada banyak objek,
  tapi setiap objek bereaksi berbeda sesuai dengan jenisnya
"""

from typing import Protocol


class MetodePembayaran(Protocol):
    # Protocol berfungsi sebagai kontrak (interface) yang menentukan
    # metode apa saja yang harus dimiliki oleh suatu objek
    # tanpa mengharuskan objek tersebut mewarisi (inherit) dari class tersebut
    def bayar(self, jumlah: float) -> None: ...

    # class MetodePembayaran bukan class biasa, melainkan sebuah Protocol
    # Protocol meyatakan bahwa setiap objek yang memiliki metode bayar dianggap sebagai MetodePembayaran


class Tunai:  # tidak perlu menulis seperti: class Tunai(MetodePembayaran)
    def bayar(self, jumlah: float) -> None:
        print(f"bayar dengan tunai jumlah: Rp. {jumlah:.0f}")


class Ewallet:
    def bayar(self, jumlah: float) -> None:
        print(f"bayar dengan E-wallet: Rp. {jumlah:.2f}")


class TransferBank:
    def bayar(self, jumlah):
        print(f"Transfer bank sebesar Rp. {jumlah:.0f}")


# method Polymorphism
def proses_bayar(metode: MetodePembayaran, jumlah: float) -> None:
    # fungsi proses_bayar tidak peduli objek apa yang dikirim,
    # selama objek tersebut memiliki metode bayar
    metode.bayar(jumlah)


tunai = Tunai()
ewallet = Ewallet()
transfer = TransferBank()

proses_bayar(tunai, 200_000)
proses_bayar(ewallet, 500_000)
proses_bayar(transfer, 150_000)

# ============================================
# Operator Overloading
"""
- Operator Overloading = memberikan perilaku khusus pada operator saat digunakan
pada objek dari class yang dibuat
- Dilakukan dengan mengimplementasikan magic method (dunder method)

Magic method yang umum:
- __add__() = penjumlahan
- __sub__() = pengurangan
- __mul__() = perkalian
_ __eq__()  = sama dengan
- __gt__()  = lebih besar dari
- __lt__()  = lebih kecil dari
- __str__() = ngeprint objek

Intinya Operator overloading membuat objek dapat menggunakan operator
bawaan python dengan perilaku yang kita
tentukan sendir
"""


class Toko:
    def __init__(self, nama: str, produk: list[str]) -> None:
        self.nama: str = nama
        self.produk: list[str] = produk

    def __add__(self, toko_lain: "Toko") -> "Toko":
        nama_baru = f"{self.nama} {toko_lain.nama}"
        produk_gabungan = self.produk + toko_lain.produk
        return Toko(nama=nama_baru, produk=produk_gabungan)

    def __str__(self) -> str:
        daftar = ", ".join(self.produk) if self.produk else "kosong"
        return f"Toko {self.nama} (produk: {daftar})"


toko_elektronik = Toko(
    "Hytam Tech", ["laptop", "keyboard", "mouse", "monitor", "Raspberry pi", "Printer"]
)

toko_buku = Toko(
    "Malas Baca",
    [
        "Volitality & Option Trading",
        "Cracking the Coding Interview",
        "10 Dosa Besar Soeharto",
    ],
)

print("=====================================")
toko_baru = toko_elektronik + toko_buku
print(toko_baru)

# ==============================================
# Methode Overriding
"""
subclass mengganti implementasi method dari superclass
"""


# superclass/parent-class
class Hewan:
    def suara(self):
        print("Suara hewan")


# subclass/child-class
class Kucing:
    def suara(self):
        print("Meong")


class Anjing(Hewan):
    def suara(self):
        print("Guk guk")


hewan = [Kucing(), Anjing()]
print("=====================================")
for h in hewan:
    h.suara()

# ========================================
# Dynamic Binding
"""
Dynamic binding = menentukan metode yang akan dipanggil saat
program dijalankan (runtime) bukan saat kode dikompilasi
"""


# SistemAlarm bertipe/berperan sebagai Protocol/blueprint
# Protocol memberi tau:
# "apapun yang dipasang sebagai alarm harus memiliki method aktif()"
class SistemAlarm(Protocol):
    def aktif(self) -> None: ...


class AlarmDefault:
    def aktif(self) -> None:
        print("bunyi sirine")


class AlarmPintar:
    def aktif(self) -> None:
        print("kirim notif ke hp")


class AlarmPihakBerwajib:
    def aktif(self) -> None:
        print("memanggil pihak berwajib")


class SmartHome:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        # jenis" alarm akan disimpan di dalam list
        self.alarm_terpasang: list[SistemAlarm] = []

    def pasang_alarm(self, alarm: SistemAlarm) -> None:
        # ketika objek memanggil method pasang_alarm,
        # alarm yang dipilih akan dimasukkan ke dalam list
        self.alarm_terpasang.append(alarm)

    # aktifkan alarm tanpa tau jenisnya
    def picu_alarm(self) -> None:
        print(f"rumah {self.owner} dalam bahaya")

        # karena alarm bertipe SistemAlarm,
        # python hanya tau: objek ini seharusny memiliki method aktif()
        # python belum tau apakah objeknya: AlarmDefault, AlarmPintar, atau AlarmPihakBerwajib
        # belum ada keputusan method mana yang akan diambil
        for alarm in self.alarm_terpasang:
            alarm.aktif()


print("==============================")
rumahA = SmartHome("Rumah A")

rumahA.pasang_alarm(AlarmDefault())
rumahA.pasang_alarm(AlarmPintar())
rumahA.pasang_alarm(AlarmPihakBerwajib())

rumahA.picu_alarm()
