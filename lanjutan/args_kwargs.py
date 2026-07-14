"""
ARGS & KWARGS

*args dan **kwargs adalah fitur Python untuk menangani argumen
fungsi yang jumlahnya tidak tetap (variadic arguments).
"""

"""
1. *args — menangkap argumen posisi ekstra sebagai tuple
Dipakai saat tidak tahu berapa banyak argumen yang akan diberikan.
"""


def jumlah(*args):
    total = 0
    for angka in args:
        total += angka
    return total


print(jumlah(1, 2, 3))  # 6
print(jumlah(10, 20, 30, 40))  # 100
print(jumlah())  # 0

"""
2. **kwargs — menangkap argumen keyword ekstra sebagai dict
Berguna untuk opsi yang fleksibel.
"""


def profil(**kwargs):
    for kunci, nilai in kwargs.items():
        print(f"  {kunci}: {nilai}")


print("Profil user:")
profil(nama="Andi", umur=25, kota="Jakarta")
#   nama: Andi
#   umur: 25
#   kota: Jakarta

"""
3. *args dan **kwargs bersamaan
Urutan parameter: posisi, *args, keyword-only, **kwargs
"""


def fungsi(a, b, *args, verbose=False, **kwargs):
    print(f"a={a}, b={b}")
    if args:
        print(f"  args: {args}")
    if verbose:
        print(f"  kwargs: {kwargs}")


fungsi(1, 2, 3, 4, verbose=True, mode="test")
# a=1, b=2
#   args: (3, 4)
#   kwargs: {'mode': 'test'}

"""
4. Unpacking dengan * — list/tuple jadi argumen posisi
Tanda * di depan iterable saat memanggil fungsi.
"""


def kali(a, b, c):
    return a * b * c


angka = [2, 3, 4]
print(kali(*angka))  # 24 (sama dengan kali(2, 3, 4))

print(*[1, 2, 3])  # 1 2 3
print(*"ABC")  # A B C

"""
5. Unpacking dengan ** — dict jadi keyword argument
Tanda ** di depan dict saat memanggil fungsi.
"""


def perkenalan(nama, umur):
    return f"{nama} berumur {umur} tahun"


data = {"nama": "Budi", "umur": 30}
print(perkenalan(**data))  # Budi berumur 30 tahun

"""
6. Wrapper / Decorator — pola umum untuk *args **kwargs
Args dan kwargs digunakan untuk meneruskan argumen ke fungsi asli.
"""


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Memanggil {func.__name__}")
        hasil = func(*args, **kwargs)
        print(f"  hasil: {hasil}")
        return hasil

    return wrapper


@logger
def tambah(a, b):
    return a + b


tambah(4, 5)
# Memanggil tambah
#   hasil: 9

"""
7. super() dengan *args dan **kwargs
Meneruskan argumen ke parent class tanpa tahu detailnya.
"""


class Animal:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def info(self):
        return f"{self.nama} ({self.jenis})"


class Kucing(Animal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.suara = "Meow"


k = Kucing("Kitty", "Anggora")
print(k.info())  # Kitty (Anggora)
print(k.suara)  # Meow

"""
8. Common pitfalls

- Urutan parameter salah:
  def salah(*args, a):  ...   # Error! *args habis menangkap semua
  def benar(a, *args): ...    # Benar

- Mutable default dengan args:
  def f(a=[]): a.append(1)    # Bahaya! list di-share antar panggilan

- ** meng-unpack non-dict:
  print(** [1, 2])            # TypeError
"""


def urutan_benar(a, b, *args):
    return (a, b, args)


print(urutan_benar(1, 2, 3, 4))  # (1, 2, (3, 4))


"""
9. __name__ == "__main__"
"""
if __name__ == "__main__":
    print("\nDemo args kwargs selesai.")
