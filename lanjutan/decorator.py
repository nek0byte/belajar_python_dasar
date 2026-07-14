"""
DECORATOR

Decorator adalah syntactic sugar Python (@) untuk menerapkan wrapper
pada fungsi/class. Memungkinkan penambahan perilaku tanpa mengubah
kode asli. Dasarnya: @decorator sama dengan func = decorator(func).
"""

"""
1. Decorator dasar
Membungkus fungsi dengan fungsi lain menggunakan syntax @.
"""


def logger(func):
    def wrapper():
        print(f"  -> {func.__name__} dijalankan")
        func()
        print(f"  <- {func.__name__} selesai")

    return wrapper


@logger
def halo():
    print("    Halo dunia!")


halo()
#   -> halo dijalankan
#     Halo dunia!
#   <- halo selesai

"""
2. Decorator dengan *args dan **kwargs
Agar decorator bisa membungkus fungsi apa pun.
"""


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"  -> {func.__name__}{args}{kwargs}")
        hasil = func(*args, **kwargs)
        print(f"  <- hasil: {hasil}")
        return hasil

    return wrapper


@logger
def tambah(a, b):
    return a + b


print(tambah(3, 4))
#   -> tambah(3, 4){}
#   <- hasil: 7
# 7


@logger
def sapa(nama, *, sopan=True):
    return f"Halo {nama}" if sopan else f"Hi {nama}"


print(sapa("Andi", sopan=False))
#   -> sapa('Andi',){'sopan': False}
#   <- hasil: Hi Andi
# Hi Andi

"""
3. functools.wraps — menjaga identitas fungsi asli
Tanpa wraps, metadata fungsi asli hilang (__name__, __doc__, dll).
"""

from functools import wraps


def logger_tanpa_wraps(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def logger_dengan_wraps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@logger_tanpa_wraps
def f1():
    """Dokumentasi f1"""
    pass


@logger_dengan_wraps
def f2():
    """Dokumentasi f2"""
    pass


print(f1.__name__)  # wrapper  (salah)
print(f1.__doc__)  # None     (hilang)
print(f2.__name__)  # f2       (benar)
print(f2.__doc__)  # Dokumentasi f2

"""
4. Decorator dengan argumen (decorator factory)
Decorator yang menerima parameter, butuh 3 level nesting.
"""


def ulang(n=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n - 1):
                func(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@ulang(n=3)
def sapa(nama):
    print(f"  Halo {nama}")


sapa("Budi")
#   Halo Budi
#   Halo Budi
#   Halo Budi

"""
5. Multiple decorators — urutan eksekusi
@a @b @c func  →  a(b(c(func)))
Eksekusi: wrapper a memanggil wrapper b yang memanggil wrapper c.
"""


def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"

    return wrapper


def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"*{func(*args, **kwargs)}*"

    return wrapper


@bold
@italic
def teks():
    return "Halo"


print(teks())  # **Halo*  → bold(italic(teks))()


@italic
@bold
def teks2():
    return "Halo"


print(teks2())  # ***Halo**  → italic(bold(teks))()

"""
6. Class-based decorator
Menggunakan class dengan method __call__ sebagai decorator.
"""


class HitungPanggilan:
    def __init__(self, func):
        self.func = func
        self.kali = 0

    def __call__(self, *args, **kwargs):
        self.kali += 1
        print(f"  Dipanggil ke-{self.kali}")
        return self.func(*args, **kwargs)


@HitungPanggilan
def katakan(isi):
    print(f"    {isi}")


katakan("Halo")  # Dipanggil ke-1 / Halo
katakan("Yak")  # Dipanggil ke-2 / Yak
print(f"Total: {katakan.kali} kali")  # Total: 2 kali

"""
7. Decorator di method class
Decorator bisa diterapkan di method, argumen pertama tetap self.
"""


def method_logger(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"[LOG] {self.__class__.__name__}.{func.__name__}")
        return func(self, *args, **kwargs)

    return wrapper


class Mobil:
    def __init__(self, merk):
        self.merk = merk

    @method_logger
    def nyalakan(self):
        print(f"  {self.merk} dinyalakan")


m = Mobil("Toyota")
m.nyalakan()  # [LOG] Mobil.nyalakan / Toyota dinyalakan

"""
8. Contoh real-world decorators
"""


# Timer — ukur durasi eksekusi
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        mulai = time.time()
        hasil = func(*args, **kwargs)
        durasi = time.time() - mulai
        print(f"  [{func.__name__}] {durasi:.4f}s")
        return hasil

    return wrapper


# Debug — cetak argumen dan hasil
def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        hasil = func(*args, **kwargs)
        print(f"  [DEBUG] {func.__name__}({args}, {kwargs}) -> {hasil}")
        return hasil

    return wrapper


# Memoize — cache hasil untuk input yang sama
def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


import time


@timer
def proses_lambat():
    time.sleep(0.05)
    return "OK"


@debug
def luas(p, l):
    return p * l


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(proses_lambat())  # [proses_lambat] 0.0500s / OK
print(luas(4, 5))  # [DEBUG] luas((4, 5), {}) -> 20 / 20
print(fibonacci(35))  # 9227465 (cepat karena cache)

"""
9. __name__ == "__main__"
"""
if __name__ == "__main__":
    print("\nDemo decorator selesai.")
