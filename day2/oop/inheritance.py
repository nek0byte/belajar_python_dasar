# Inheritance
# ========================================
class Kendaraan:
    def __init__(self, merk: str, max_speed: int) -> None:
        self.merk: str = merk
        self.max_speed: int = max_speed
        self.berjalan: bool = False

    def start(self) -> None:
        self.berjalan = True
        print(f"{self.merk} telah dinyalakan")

    def stop(self) -> None:
        self.berjalan = False
        print(f"{self.merk} telah dimatikan")


class Mobil(Kendaraan):
    def __init__(self, merk: str, max_speed: int, warna: str) -> None:
        super().__init__(merk, max_speed)
        self.warna: str = warna

    def klakson(self) -> None:
        print("{self.merk} membunyikan klakson: Beep-beep")


mobil = Mobil("Hell Cat", 200, "Merah")
mobil.start()
mobil.stop()


# ========================================
# Multi inheritance
"""
sebuah class bisa mewarisi lebih dari 1 class induk
"""


class Penyihir:
    def lempar_spell(self) -> None:
        print("melempar spell: Avada Cadabra!!!")


class Petarung:
    def serang(self) -> None:
        print("menyerang dengan pedang!!!")


# class dengan multi inheritance
class Player(Penyihir, Petarung):
    def gunakan_skill_multi(self) -> None:
        print("kombinasi serangan!!!")
        self.lempar_spell()
        self.serang()


hero1 = Player()
hero1.gunakan_skill_multi()
