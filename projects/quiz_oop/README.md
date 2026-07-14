# Quiz OOP — Versi OOP dari Quiz CLI

Aplikasi kuis matematika berbasis CLI menggunakan **Object-Oriented Programming**.
Versi OOP refactored dari `projects/quiz/quiz.py`.

## Struktur Project

```
quiz_oop/
├── quiz_oop.py     # 92 baris — class Soal, SoalUjian, AplikasiUjianSekolah
└── bank_soal.txt   # 50 soal (format: pertanyaan|jawaban1,jawaban2,jawaban3,jawaban4)
```

## Cara Kerja Kode

### `class Soal` — Representasi satu soal

Setiap soal memiliki pertanyaan, daftar jawaban (diacak saat init), dan
jawaban benar. Method `cek_jawaban()` membandingkan input user dengan
jawaban yang benar.

```python
class Soal:
    def __init__(self, pertanyaan, jawaban, jawaban_benar):
        self.pertanyaan = pertanyaan
        self.jawaban = jawaban
        self.jawaban_benar = jawaban_benar
        random.shuffle(self.jawaban)

    def cek_jawaban(self, jawaban_user):
        return jawaban_user == self.jawaban_benar
```

### `class SoalUjian` — Kumpulan soal ujian

Menerima daftar soal mentah dari file, mengacak urutan, memilih 10 soal
(atau kurang jika file < 10), mem-parse format `pertanyaan|jwb1,jwb2,...`,
lalu membuat objek `Soal` untuk setiap soal.

```python
class SoalUjian:
    def __init__(self, soal_asli):
        self.daftar_soal = []
        random.shuffle(soal_asli)
        jumlah_soal = min(10, len(soal_asli))
        for i in range(jumlah_soal):
            soal = soal_asli[i]
            data = soal.split("|")
            jawaban = data[1].split(",")
            jawaban_benar = jawaban[0]
            soal_obj = Soal(data[0], jawaban, jawaban_benar)
            self.daftar_soal.append(soal_obj)
```

### `class AplikasiUjianSekolah` — CLI utama

Membaca file soal, membuat `SoalUjian`, lalu menjalankan loop ujian:
tampilkan soal, terima jawaban, validasi input, hitung skor.

```python
class AplikasiUjianSekolah:
    def __init__(self, file_soal):
        # baca file, parse, buat SoalUjian
        ...

    def run(self):
        for i, soal in enumerate(self.soal_ujian.daftar_soal):
            print(soal.pertanyaan)
            # tampilkan opsi A/B/C/D
            # terima input user (loop sampai valid)
            # cek jawaban, akumulasi skor
        # tampilkan hasil
```

### Error Handling

- **Path absolut** — `os.path.join(os.path.dirname(__file__), ...)` agar
  file bisa dijalankan dari folder mana pun
- **Validasi input** — `while True` + `.upper()` + `in opsi` — tidak
  crash jika user input `e`, `a`, atau karakter lain
- **Jumlah soal** — `min(10, len(soal_asli))` aman jika file < 10 soal

## Perbedaan dari `quiz.py`

| Aspek                     | `quiz.py` (prosedural)                    | `quiz_oop.py` (OOP)                        |
|---------------------------|-------------------------------------------|--------------------------------------------|
| **Representasi data**     | Dictionary `{pertanyaan, jawaban, ...}`   | Class `Soal` dengan method `cek_jawaban()` |
| **Arsitektur**            | Fungsi-fungsi modular                     | 3 class dengan tanggung jawab terpisah     |
| **Encapsulation**         | Data diakses langsung via `soal["..."]`   | Data diakses via atribut class             |
| **Logika soal**           | Di `buat_soal()` — fungsi biasa           | Di `Soal.__init__()` + `SoalUjian`         |
| **Entry point**           | `app_ujian()` dipanggil langsung          | `AplikasiUjianSekolah().run()`             |
| **Reusability**           | Rendah — fungsi terkait erat              | Tinggi — class bisa di-extend/di-test      |
| **Parser soal**           | Inline di `buat_soal()`                   | Di `SoalUjian.__init__()`                  |
| **Jumlah baris**          | 87 baris                                  | 92 baris                                   |

### Poin Refactoring Utama

1. **Dari dict ke class** — data soal direpresentasikan sebagai objek
   `Soal` dengan method `cek_jawaban()` dan inisialisasi otomatis
2. **Separation of Concerns** — `Soal` (data), `SoalUjian` (koleksi +
   parser), `AplikasiUjianSekolah` (CLI + skor)
3. **Encapsulation** — logika pengacakan jawaban di dalam `Soal.__init__`,
   tidak di fungsi terpisah
4. **Path absolut + validasi input** — di-port dari `quiz.py` setelah
   perbaikan error

### Kekurangan yang Tersisa

- **Persistence** — data soal hanya dari file statis, tidak ada
  penyimpanan hasil ujian
- **Single file** — semua class masih dalam satu file (bisa dipecah
  untuk proyek lebih besar)

## Cara Menjalankan

```bash
cd projects/quiz_oop
python quiz_oop.py
```
