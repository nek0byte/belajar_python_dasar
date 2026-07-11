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
    # fungsi proses_bayar tidak peduli objek apa yang dikirim, selama objek tersebut memiliki metode bayar
    metode.bayar(jumlah)


tunai = Tunai()
ewallet = Ewallet()
transfer = TransferBank()

proses_bayar(tunai, 200_000)
proses_bayar(ewallet, 500_000)
proses_bayar(transfer, 150_000)

# ============================================
# Operator Overloading


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

toko_baru = toko_elektronik + toko_buku
print(toko_baru)
