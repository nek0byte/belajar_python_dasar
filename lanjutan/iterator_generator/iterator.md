## Iterator & generator

### Iterable
iterable adalah objek yang bisa diulang menggunaka for loop.
contoh:
```
angka = [1, 2, 3, 4, 5]
nama = ("aa", "bb")
huruf = "python"

for i in angka:
    print(i)
```
semua objek di atas adalah iterable.

### Iterator
iterator adalah object yang mengambil data dari iterable satu per satu.
iterator memiliki dua method penting:
- `__next__()`
- `__iter__()`
contoh:
```
angka = [10, 20, 30]

it = iter(angka)

print(next(it))
print(next(it))
print(next(it))
```

output:
```
10
20
30
```
jika dipanggil lagi akan error:
```
next(it
```
akan muncul `StopIteration`

## Cara kerja for
ketika kita menulis:
```
for i in angka:
    print(i)
```
python akan mengeksekusi `__iter__()` dan `__next__()`.
```
it = iter(angka)

while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break
```

### Generator
generator adalah cara yang lebih mudah membuat iterator.
daripada membuat class dan implementasi `__iter__()` dan `__next__()`.
generator menggunakan keyword `yield`.

contoh:
```
def counter(batas):
    angka = 1

    while angka <= batas:
        yield angka
        angka += 1
```
pemakaian:
```
for i in counter(5):
    print(i)
```

### apa itu yield?
`yield` mirip seperti `return`, tapi `yield` tidak akan menghentikan eksekusi program.
```
fungsi berhenti sementara
↓
dipanggil lagi
↓
lanjut dari posisi terakhir
```

