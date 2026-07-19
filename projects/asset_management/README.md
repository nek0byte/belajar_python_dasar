# Asset Management

Aplikasi CLI untuk mengelola aset perusahaan: **Kendaraan**, **Elektronik**,
dan **Tanah Bangunan**.

## Struktur Project

```
asset_management/
├── main.py         #   6 baris — entry point
├── models.py       #  50 baris — class Aset, subclass, DaftarAset
├── views.py        # 123 baris — semua fungsi input/output/display
└── controllers.py  # 110 baris — logika bisnis (CRUD)
```

## MVC Architecture

```
┌─────────────────────────────────────────────────────┐
│                      main.py                        │
│            membuat AsetController lalu run()         │
└─────────────────────┬───────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│  controllers.py          ────►  models.py            │
│  AsetController                 Aset, AsetKendaraan, │
│  • run()                       AsetElektronik,       │
│  • tambah_aset()               AsetTanahBangunan,    │
│  • lihat_aset()                DaftarAset             │
│  • ubah_aset()                                        │
│  • hapus_aset()                                       │
│       │                                               │
│       │ memanggil fungsi I/O                          │
│       ▼                                               │
│  views.py                    ┌────────────────────────┤
│  • tampilkan_menu_*()       │  Type hints di semua    │
│  • input_aset_*()           │  parameter & return     │
│  • input_int() / input_kode() (str, int, Optional)    │
│  • input_int_opsi()         └────────────────────────┤
│  • tampilkan_*()                                     │
│  • tampilkan_pesan()                                  │
└─────────────────────────────────────────────────────┘
```

### Peran Masing-Masing Layer

| Layer | Tanggung Jawab | Contoh |
|-------|---------------|--------|
| **Model** (`models.py`) | Definisi data + koleksi | `Aset` (kode, nama, harga), `DaftarAset` (tambah, ambil, hapus) |
| **View** (`views.py`) | Semua I/O dengan user | Tampilkan menu, input form, validasi angka, display detail aset |
| **Controller** (`controllers.py`) | Logika bisnis + orkestrasi | Terima input dari View, proses via Model, kirim hasil ke View |
| **Entry** (`main.py`) | Titik masuk program | Buat Controller, panggil `run()` |

## Cara Kerja Kode

### `models.py` — Model (Data Layer)

`Aset` adalah base class dengan 3 subclass yang mewarisi atribut `kode`,
`nama`, `harga` dan menambah atribut spesifik:

```python
class Aset:
    def __init__(self, kode: str, nama: str, harga: int): ...

class AsetKendaraan(Aset):     # + stkn, tahun
class AsetElektronik(Aset):    # + serial_number
class AsetTanahBangunan(Aset): # + sertifikat, njop, luas
```

`DaftarAset` mengelola koleksi aset dalam list dengan method:

- `tambah_aset(aset)` — menambah ke daftar
- `ambil_aset(kode)` — mencari aset by kode, return `Optional[Aset]`
- `hapus_aset(kode)` — menghapus aset by kode, return `bool`

### `views.py` — View (UI Layer)

Semua fungsi untuk berinteraksi dengan user, dipisah berdasarkan
fungsi:

- **Validasi input**: `input_int()` — loop `try/except` sampai dapat
  angka valid; `input_int_opsi()` — hanya terima dalam range tertentu
- **Form input**: `input_aset_kendaraan()`, `input_aset_elektronik()`,
  `input_aset_tanah_bangunan()` — masing-masing return tuple data
- **Display**: `tampilkan_aset_kendaraan(aset)`, dll — cetak detail
  aset sesuai tipe
- **Menu**: `tampilkan_menu_utama()`, `tampilkan_menu_tambah()`,
  `tampilkan_menu_setelah_lihat()`

Tidak ada logika bisnis di View — semua fungsi hanya menerima data
dan menampilkan/meminta input.

### `controllers.py` — Controller (Business Logic Layer)

`AsetController` adalah otak aplikasi. Setiap method mewakili satu
skenario use case:

- **`run()`** — loop utama, tampilkan menu, arahkan ke method sesuai
  pilihan
- **`tambah_aset()`** — tampilkan menu tambah, panggil View untuk
  input data, buat objek Model, simpan via `DaftarAset`
- **`lihat_aset()`** — iterasi `DaftarAset`, panggil View display
  sesuai tipe (`isinstance`), lalu tampilkan menu ubah/hapus
- **`ubah_aset()`** — cari aset by kode, panggil View untuk input
  data baru, update atribut Model
- **`hapus_aset()`** — cari aset by kode, hapus via `DaftarAset`,
  tampilkan pesan hasil

```python
class AsetController:
    def __init__(self):
        self.daftar_aset = DaftarAset()

    def tambah_aset(self):
        data = views.input_aset_kendaraan()
        aset = AsetKendaraan(*data)
        self.daftar_aset.tambah_aset(aset)
        views.tampilkan_pesan("Kendaraan berhasil ditambahkan")
```

### `main.py` — Entry Point

Minimal — hanya import Controller dan menjalankannya:

```python
from controllers import AsetController

if __name__ == "__main__":
    app = AsetController()
    app.run()
```

## Fitur

- **CRUD 3 tipe aset** — Kendaraan, Elektronik, Tanah Bangunan
- **Input validation** — semua input angka di-protect `try/except`,
  menu hanya terima range valid

### Kekurangan

- **Persistence** — data hilang saat program ditutup (in-memory)

## Cara Menjalankan

```bash
cd projects/asset_management
python main.py
```
