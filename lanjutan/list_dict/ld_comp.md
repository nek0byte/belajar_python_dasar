# comprehension
comprehension adalah cara singkat dan lebih "Pythonic" untuk membuat koleksi (list, set, dict) dari iterable. Dibandingkan menggunakan for biasa, kode menjadi lebih ringkas dan mudah dibaca.

## List comprehension
syntax:
```
[ekspresi for item in iterable]
```
contoh:
tanpa list comprehension:
```
angka = []
for i in range(5):
    angka.append(i)
```
dengan list comprehension:
```
angka = [i for i in range(5)]
angka = [i * i for i in range(5)]
angka = [i * 2 for i in range(5)]
```

### menggunakan if
```
angka = [i for i in range(5) if i % 2 == 0]
angka = [i for i in range(5) if i % 2 != 0]
```
### if else di comprehension
```
angka = ["genap" if i % 2 == 0 else "ganjil" for i in range(5)]
angka = ["ganjil" if i % 2 != 0 else "genap" for i in range(5)]
```

## Dictionary comprehension
syntax:
```
{key: value for item in iterable}
```
### dict dengan kondisi
```
angka = {i: i * i for i in range(5)}
angka = {i: i * 2 for i in range(5)}
angka = {i: "genap" if i % 2 == 0 else "ganjil" for i in range(5)}
```
### ganti nilai dict
misal:
```
nilai = {
    "a": 1,
    "b": 2,
    "c": 3
}
```
naik 5 poin:
```
baru = {
    nama: skor + 5 for nama, skor in nilai.items()
}
```


## kapan menggunakan comprehension?
- Membuat list atau dictionary baru dari iterable.
- Melakukan transformasi sederhana (misalnya mengalikan, mengubah huruf besar, atau memfilter data).
- Kode yang tetap mudah dibaca meskipun ditulis dalam satu baris.
