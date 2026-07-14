"""
MODUL & IMPORT

Modul adalah file .py yang berisi kode Python (fungsi, kelas, variabel).
Dengan import, kita bisa menggunakan kode dari file lain.
"""

"""
1. import module
Mengimpor seluruh modul. Fungsi dipanggil dengan module.fungsi()
"""
import math

print(math.sqrt(25))  # 5.0
print(math.factorial(5))  # 120

"""
2. import module as alias
Memberi nama pendek untuk modul
"""
import math as m

print(m.pi)  # 3.141592653589793
print(m.e)  # 2.718281828459045

"""
3. from module import sesuatu
Mengimpor hanya fungsi/variabel tertentu (tanpa prefix module)
"""
from math import sqrt, pi

print(sqrt(16))  # 4.0
print(pi)  # 3.141592653589793

"""
4. from module import sesuatu as alias
Memberi alias pada fungsi yang diimpor
"""
from math import pow as pangkat

print(pangkat(2, 10))  # 1024.0

"""
5. from module import *  (wildcard)
Mengimpor SEMUA nama publik dari modul (TIDAK disarankan)
Karena bisa menimpa (override) nama fungsi/variabel kita sendiri
"""
from math import *

print(sin(0))  # 0.0
print(cos(0))  # 1.0
print(log(1))  # 0.0

"""
6. Mengimpor banyak item sekaligus
"""
from math import floor, ceil, trunc, gcd, lcm

print(floor(3.7))  # 3
print(ceil(3.2))  # 4
print(gcd(12, 8))  # 4

"""
7. Mengimpor modul buatan sendiri
File: loop_func.py  ->  berisi fungsi fac(), my_function4()
"""
from loop_func import fac, my_function4

print(fac(5))  # 120
print(my_function4(fname="Tobias", lname="Refsnes"))

"""
8. Mengimpor semua fungsi dari modul sendiri
"""
from loop_func import *

"""
9. __name__ == "__main__"  — Proteksi eksekusi

Apa itu __name__?
- Saat Python menjalankan suatu file, Python membuat variabel __name__
- Jika file di-RUN langsung:   __name__ = "__main__"
- Jika file di-IMPORT:         __name__ = "nama_file" (misal "modul_import")

Kenapa penting?
- Kode tes / print di dalam if __name__ == "__main__" TIDAK akan jalan
  saat file di-import, sehingga tidak mengganggu file lain.
- Berguna untuk membuat file yang bisa berfungsi ganda:
  a) Sebagai modul (di-import) — hanya menyediakan fungsi/kelas
  b) Sebagai script utama (di-run langsung) — menjalankan demo/test

Contoh praktis:
  if __name__ == "__main__":
      print("Tes:", fac(5))
      print("Tes:", my_function4("John", "Doe"))
"""
if __name__ == "__main__":
    print("File ini dijalankan langsung, bukan diimpor.")

"""
10. sys.path — Di mana Python mencari modul?
"""
import sys

print(sys.path)  # daftar folder yang dicari Python

"""
Kita bisa menambah folder sendiri:
  sys.path.append("/path/ke/folder")
"""

"""
11. Membuat modul ulang / reload (saat development)
"""
import importlib
# importlib.reload(nama_modul)  # memuat ulang modul tanpa restart

"""
12. help() — Melihat isi modul
"""
# help(math)   # uncomment untuk lihat dokumentasi modul math
# print(dir(math))  # lihat semua nama yang ada di modul math
