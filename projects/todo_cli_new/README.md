# Todo CLI — Refactored Version (`todo_cli_new`)

CLI To-Do List berbasis Python. Versi refactored dari `todo_cli` dengan
arsitektur modular dan pendekatan OOP.

## Struktur Project

```
todo_cli_new/
├── models.py         # 13 baris — definisi class Task
├── task_manager.py   # 50 baris — logika CRUD + manajemen data
└── main.py           # 120 baris — CLI / antarmuka pengguna
```

## Cara Kerja Kode

### `models.py` — Class `Task`

Representasi data task menggunakan **class**, bukan dictionary.

```python
class Task:
    def __init__(self, id, judul):
        self.id = id
        self.judul = judul
        self.selesai = False

    def tandai_selesai(self):
        self.selesai = True

    def __str__(self):
        status = "Selesai" if self.selesai else "Belum selesai"
        return f"[{self.id}] {self.judul} - {status}"
```

Method `tandai_selesai()` mengubah status, dan `__str__()` mengatur
format tampilan (dipakai otomatis saat `print(task)`).

### `task_manager.py` — CRUD (Create, Read, Update, Delete) Logic

Memisahkan logika bisnis dari antarmuka. Berisi:

- `generate_id()` — menghasilkan ID baru berdasarkan `max(task.id) + 1`,
  sehingga tidak ada ID duplikat meskipun task dihapus
- `tambah_task(judul)` — membuat objek `Task` dan menambahkannya ke list
- `lihat_task()` — mengembalikan seluruh list task
- `cari_task(keyword)` — mencari task berdasarkan substring judul
  (case-insensitive)
- `edit_task(id_task, judul_baru)` — mengubah judul task
- `selesai_task(id_task)` — menandai task sebagai selesai
- `hapus_task(id_task)` — menghapus task dari list

Semua fungsi mengembalikan nilai boolean atau objek, bukan langsung
mencetak ke layar — ini membuatnya reusable.

```python
from models import Task

tasks = []

def tambah_task(judul):
    task = Task(generate_id(), judul)
    tasks.append(task)
    return task
```

### `main.py` — CLI Entry Point

Menangani interaksi dengan pengguna (input/output) dengan memanggil
fungsi dari `task_manager`. Dilengkapi error handling:

- `try/except ValueError` di menu 4/5/6 — mencegah crash saat input
  ID bukan angka
- `if not tasks` di menu 4/5/6 — tidak langsung minta ID jika task
  kosong
- Validasi judul kosong (`.strip()`) di menu 1 dan 4
- Validasi keyword kosong di menu 3
- `try/except KeyboardInterrupt` — menangani Ctrl+C dengan rapi

```python
import task_manager

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul = input("Nama task: ").strip()
            if not judul:
                print("Nama task tidak boleh kosong")
                continue
            task_manager.tambah_task(judul)
            print("Task berhasil ditambahkan")

        elif pilihan == "4":
            if not task_manager.lihat_task():
                print("Belum ada task")
                continue
            try:
                id_task = int(input("ID task: "))
            except ValueError:
                print("ID harus berupa angka")
                continue

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram dihentikan pengguna")
```

## Perbedaan dari `todo_cli`

| Aspek                     | `todo_cli` (lama)                        | `todo_cli_new` (baru)                       |
|---------------------------|------------------------------------------|---------------------------------------------|
| **Arsitektur**            | Monolitik — 1 file (150 baris)           | Modular — 3 file dengan tanggung jawab jelas|
| **Representasi data**     | Dictionary `{id, judul, selesai}`        | Class `Task` + method `tandai_selesai()`    |
| **ID generation**         | `len(tasks) + 1` — rawan konflik         | `max(task.id) + 1` — aman                   |
| **Fitur search**          | Tidak ada                                | Ada — `cari_task()` case-insensitive        |
| **Edit judul**            | Tidak ada                                | Ada — `edit_task(id, judul_baru)`           |
| **Menu**                  | 5 menu                                   | 7 menu (+ Cari, Edit)                       |
| **Guard `__name__`**      | Tidak ada — `main()` dipanggil langsung   | Ada — `if __name__ == "__main__"`           |
| **Error handling**        | `try/except ValueError`                  | try/except ValueError + guard if not tasks + validasi input kosong + KeyboardInterrupt |
| **Output format**         | `[id] \| judul - status`                | `[id] judul - status`                       |
| **Tampilan menu**         | Inline `print()`                         | Multi-line string                           |

### Poin Refactoring Utama

1. **Separation of Concerns** — data model (`models.py`), business
   logic (`task_manager.py`), dan UI (`main.py`) dipisah ke file
   berbeda
2. **Dari dict ke class** — data task kini direpresentasikan sebagai
   objek `Task` dengan method dan `__str__`
3. **Fungsi return value** — fungsi di `task_manager` mengembalikan
   nilai, bukan langsung mencetak; sehingga lebih mudah di-test ulang
4. **ID aman** — `max() + 1` menggantikan `len() + 1` agar tidak ada
   ID ganda setelah penghapusan
5. **Fitur baru** — pencarian keyword dan edit judul tersedia
6. **Error handling lebih lengkap** — tidak hanya `try/except`, tapi
   juga validasi input kosong, guard list kosong, dan KeyboardInterrupt

### Kekurangan yang Tersisa

- **Persistence** — data masih in-memory (hilang saat program ditutup)

## Cara Menjalankan

```bash
cd projects/todo_cli_new
python main.py
```
