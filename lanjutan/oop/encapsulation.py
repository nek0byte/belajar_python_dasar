# encapsulation
"""
membungkus data (atribut) dan method dalam satu class
serta membatasi akses langsung ke data tersebut.

agar data tetap aman dan hanya bisa dibubah melalui
cara yang gtelah ditentukan oleh class.
"""

from datetime import date, datetime
from enum import Flag
from typing import Optional


class RekeningBank:
    def __init__(self, nasabah: str, saldo_awal: int, pin: str) -> None:
        self.__nasabah: str = nasabah
        self.__saldo: int = saldo_awal
        self.__pin: str = pin

        self._riwayat_transaksi: list = []

    def cek_saldo(self, pin: str) -> Optional[int]:
        if self.__verifikasi_pin(pin):
            return self.__saldo
        print("pin salah")
        return None

    def setor_tunai(self, jumlah: int) -> None:
        if jumlah <= 0:
            print("jumlah tidak valid")
            return
        self.__saldo += jumlah
        self._tambah_riwayat(f"setor -> +Rp. {jumlah}")
        print(f"setor tunai Rp. {jumlah} berhasil!")

    def tarik_tunai(self, jumlah: int, pin: str) -> bool:
        if not self.__verifikasi_pin(pin):
            print("pin salah!")
            return False
        if jumlah <= 0 or jumlah > self.__saldo:
            print("jumlah tidak valid / saldo tidak cukup")
            return False

        self.__saldo -= jumlah
        self._tambah_riwayat(f"tarik tunai: -Rp. {jumlah}")
        print(f"tarik tunai Rp. {jumlah} berhasil")
        return True

    def __verifikasi_pin(self, pin_input: str) -> bool:
        return pin_input == self.__pin

    def _tambah_riwayat(self, transaksi: str) -> None:
        waktu = datetime.now().strftime("%H:%M")
        self._riwayat_transaksi.append(f"[{waktu} - {transaksi}]")


orang = RekeningBank("Orang", 15_000_000, "123")

orang.setor_tunai(1_000_000)
orang.tarik_tunai(2_000_000, "321")
