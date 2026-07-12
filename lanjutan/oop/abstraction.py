# Abstaction
"""
menyembunyikan detail implementasi dan hanya
menampilkan hal" yang penting(intreface) kepada pengguna
"""

from abc import ABC, abstractmethod


class Pembayaran(ABC):
    """
    class Pembayaran adalah sebuah abstract class (ABC)
    yang artinya Pembayaran mendefinisikan:
        - apa yang harus dimiliki oleh semua metode pembayaran
        - tetapi tidak menentukan bagaimana cara pembayaran dilakukan
    """

    @abstractmethod
    def proses_pembayaran(self, jumlah: int) -> bool:
        pass

    """
    method proses_pembayaran dibuat menjadi abstract method karenan setiap
    metode pembayaran memiliki proses yang berbeda.
    Maka di class abstract cukup ditulis: 
    @abstractmethod
    def proses_pembayaran(): pass
    """

    def validasi_jumlah(self, jumlah: int) -> bool:
        return jumlah > 0

    """
    methode validasi_jumlah tidak abstract karena semua metode pembayaran
    bisa menggunakan validasi yang sama.
    metode ini sudah memiliki implementasi sehingga dapat diwariskan ke semua subclass
    """


class Ewallet(Pembayaran):
    def proses_pembayaran(self, jumlah: int) -> bool:
        if not self.validasi_jumlah(jumlah):
            print("jumlah tidak valid")
            return False

        print(f"Pembayaran via E-wallet dengan total Rp. {jumlah} valid")
        print("pembayaran berhasil.")
        return True


class Tunai(Pembayaran):
    def proses_pembayaran(self, jumlah: int) -> bool:
        if not self.validasi_jumlah(jumlah):
            print("jumlah tidak sesuai")
            return False
        print(f"pembayaran tunai sebesar Rp. {jumlah} berhasil.")
        return True


def bayar(pembayaran: Pembayaran, jumlah: int) -> None:
    pembayaran.proses_pembayaran(jumlah)


ewallet = Ewallet()
bayar(ewallet, 150_000)

tunai = Tunai()
bayar(tunai, 200_000)
