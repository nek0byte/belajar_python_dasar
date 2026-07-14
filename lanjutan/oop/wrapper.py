"""
WRAPPER

Wrapper adalah fungsi atau class yang membungkus fungsi/class lain
untuk menambah perilaku tanpa mengubah kode aslinya. Ini adalah
konsep dasar dari decorator.
"""

"""
1. Wrapper function sederhana
Fungsi yang menerima fungsi lain dan menjalankannya di dalamnya.
"""


def sapa(func):
    def inner():
        print("Halo!")
        func()
        print("Sampai jumpa!")

    return inner


def nama():
    print("  Saya Andi")


cetak = sapa(nama)
cetak()
# Halo!
#   Saya Andi
# Sampai jumpa!

"""
2. Wrapper dengan *args dan **kwargs
Agar wrapper bisa membungkus fungsi apa pun, terima args/kwargs.
"""


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Memanggil {func.__name__}")
        hasil = func(*args, **kwargs)
        print(f"[LOG] Selesai: {hasil}")
        return hasil

    return wrapper


def tambah(a, b):
    return a + b


logged_tambah = logger(tambah)
print(logged_tambah(3, 4))  # [LOG] Memanggil tambah / [LOG] Selesai: 7 / 7

"""
3. Wrapper untuk validasi
Memeriksa input sebelum fungsi dijalankan.
"""


def validasi_positif(func):
    def wrapper(*args, **kwargs):
        for nilai in args:
            if nilai < 0:
                raise ValueError("Nilai harus positif")
        return func(*args, **kwargs)

    return wrapper


def akar(x):
    return x**0.5


akar_aman = validasi_positif(akar)
print(akar_aman(9))  # 3.0
# print(akar_aman(-4))  # ValueError: Nilai harus positif

"""
4. Wrapper untuk logging eksekusi
Mencatat waktu mulai, parameter, dan durasi.
"""

import time


def timer(func):
    def wrapper(*args, **kwargs):
        mulai = time.time()
        hasil = func(*args, **kwargs)
        durasi = time.time() - mulai
        print(f"[TIMER] {func.__name__}: {durasi:.4f} detik")
        return hasil

    return wrapper


def lambat():
    time.sleep(0.1)
    return "selesai"


lambat_tercatat = timer(lambat)
print(lambat_tercatat())
# [TIMER] lambat: 0.1001 detik
# selesai

"""
5. Wrapper untuk mengubah output
Memodifikasi hasil yang dikembalikan fungsi asli.
"""


def tebal(func):
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"

    return wrapper


def miring(func):
    def wrapper(*args, **kwargs):
        return f"*{func(*args, **kwargs)}*"

    return wrapper


def halo(nama):
    return f"Halo {nama}"


print(tebal(halo)("Budi"))  # **Halo Budi**
print(miring(tebal(halo))("Budi"))  # ***Halo Budi***

"""
6. Wrapper class
Class yang menerima objek dan mendelegasikan method ke objek tersebut.
"""


class LoggerWrapper:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, nama):
        attr = getattr(self._obj, nama)
        if callable(attr):

            def wrapper(*args, **kwargs):
                print(f"[LOG] {nama} dipanggil")
                return attr(*args, **kwargs)

            return wrapper
        return attr


class Kalkulator:
    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b


k = LoggerWrapper(Kalkulator())
print(k.tambah(3, 4))  # [LOG] tambah dipanggil / 7
print(k.kurang(10, 3))  # [LOG] kurang dipanggil / 7

"""
7. Wrapper real-world — retry otomatis
Mengulang fungsi jika gagal (misal karena network error).
"""

import random


def retry(maks=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for percobaan in range(1, maks + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  Percobaan {percobaan} gagal: {e}")
                    if percobaan == maks:
                        raise
            return None

        return wrapper

    return decorator


def unreliable_request():
    if random.random() < 0.7:
        raise ConnectionError("Timeout")
    return "Data berhasil"


# Dengan retry, fungsi akan dicoba ulang sampai 3x
# (uncomment untuk lihat)
# aman = retry(3)(unreliable_request)
# print(aman())

"""
8. Wrapper vs Decorator

Wrapper = konsep umum: fungsi/class yang membungkus yang lain.
Decorator = syntactic sugar Python (@) untuk menerapkan wrapper.

@decorator
def f(): pass

sama dengan:

def f(): pass
f = decorator(f)

Decorator adalah wrapper yang diterapkan dengan syntax @.
"""

"""
9. __name__ == "__main__"
"""

if __name__ == "__main__":
    print("\nDemo wrapper selesai.")
