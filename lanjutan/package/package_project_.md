## python package & project structure
package adalah folder yang berisi berbagai modul python `__init__.py` dan file lainnya.

contoh:
```
my_package/
|
|-- __init__.py
|-- math_utils.py
|-- string_utils.py
|-- file_utils.py
```

`__init__.py` digunakan untuk mengatur import pada package.

contoh:
```
from my_package import math_utils
from my_package import string_utils
from my_package import file_utils
```

### contoh struktur project:
```
my_project/
│
├── pyproject.toml
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt        # optional
│
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── models.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── api.py
│       ├── utils/
│       │   ├── __init__.py
│       │   └── helpers.py
│       └── database/
│           ├── __init__.py
│           └── db.py
│
├── tests/
│   ├── test_api.py
│   └── test_utils.py
│
└── docs/
```

"**src layout**" ini direkomendasikan karena membantu untuk menanggulangi meng-import kode secara langsung ke package.


| File | Tujuan |
|------|--------|
| `__init__.py` | Menyediakan moadul `__init__.py` untuk mengatur import pada package |
| `main.py` | Menyediakan fungsi utama |
| `config.py` | Menyediakan konfigurasi |
| `models.py` | Menyediakan model |
| `services/api.py` | Menyediakan fungsi untuk API |
| `utils/helpers.py` | Menyediakan fungsi helper |
| `database/db.py` | Menyediakan fungsi untuk database |
| `pyproject.toml` | Menyediakan konfigurasi pyproject |
| `README.md` | Menyediakan deskripsi proyek |
| `LICENSE` | Menyediakan lisensi proyek |
| `.gitignore` | Menyediakan file untuk mengabaikan file dan folder tertentu |
| `requirements.txt` | Menyediakan file untuk menginstal dependensi |
| `docs/` | Menyediakan dokumentasi proyek |


### contoh organisasi package
```
src/
└── inventory/
    ├── __init__.py
    ├── cli.py
    ├── models.py
    ├── repository.py
    ├── service.py
    ├── exceptions.py
    ├── config.py
    ├── utils.py
    └── api/
        ├── __init__.py
        ├── routes.py
        └── auth.py
```
setiap modul memiliki fungsi yang jelas:
- `models.py` -- menyediakan model
- `repository.py` -- menyediakan repository
- `service.py` -- menyediakan service
- `exceptions.py` -- menyediakan exception
- `config.py` -- menyediakan konfigurasi
- `utils.py` -- menyediakan fungsi helper

### import style
absolute import = import dari luar folder
```
from inventory.repository import InventoryRepository
from inventory.service import InventoryService
```

relative import = import dari folder yang sama
```
from .repository import InventoryRepository
from .service import InventoryService
```


### __init__.py lebih dalam

`__init__.py` bisa digunakan untuk berbagai keperluan:

**1. Mengatur `__all__`** — membatasi apa yang di-export saat `from package import *`:
```python
# my_package/__init__.py
__all__ = ["math_utils", "string_utils"]
```

**2. Auto-import submodule** — memudahkan akses dari luar:
```python
# my_package/__init__.py
from .math_utils import faktor
from .string_utils import kapital

__all__ = ["faktor", "kapital"]
```
Pengguna bisa langsung:
```python
from my_package import faktor
```

**3. Inisialisasi package** — kode di `__init__.py` jalan sekali saat package di-import:
```python
# my_package/__init__.py
print(f"my_package v1.0.0 di-load")
```


### __main__.py — menjalankan package dengan `python -m`

Jika package memiliki file `__main__.py`, package bisa di-run langsung:
```
my_package/
├── __init__.py
├── __main__.py     # python -m my_package
└── cli.py
```

```python
# __main__.py
from .cli import main

if __name__ == "__main__":
    main()
```

Cara menjalankan:
```bash
python -m my_package
```


### Namespace package (PEP 420)

Package **tanpa** `__init__.py`. Berguna saat satu package terpecah di beberapa folder berbeda:

```
proyek-a/
└── my_package/
    └── modul_a.py

proyek-b/
└── my_package/
    └── modul_b.py
```

Keduanya bisa diakses sebagai satu package:
```python
import my_package.modul_a
import my_package.modul_b
```

Ciri-ciri namespace package:
- Tidak punya `__init__.py`
- Bisa berasal dari beberapa direktori berbeda di `sys.path`
- Cocok untuk plugin / ekstensi yang terpisah


### Instalasi package lokal — `pip install -e .`

Agar package bisa di-import dari mana saja tanpa repot mengatur `sys.path`:

```bash
cd my_project
pip install -e .
```

Flag `-e` (editable) membuat perubahan kode langsung terlihat tanpa perlu install ulang.
Ini adalah cara terbaik untuk development.

File `pyproject.toml` minimal:
```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "my_project"
version = "0.1.0"
dependencies = [
    "requests>=2.28",
]
```


### pyproject.toml detail

File konfigurasi utama proyek Python modern (pengganti `setup.py`):

```toml
[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my_project"
version = "0.1.0"
description = "Deskripsi proyek"
readme = "README.md"
license = {text = "MIT"}
authors = [{name = "Nama", email = "email@example.com"}]
requires-python = ">=3.10"
dependencies = [
    "flask>=3.0",
    "sqlalchemy>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "black",
]

[project.scripts]
my-cli = "my_project.cli:main"
```

| Field | Fungsi |
|-------|--------|
| `[build-system]` | Menentukan backend build (setuptools, poetry, pdm, dll) |
| `name` | Nama package di PyPI |
| `version` | Versi package |
| `dependencies` | Dependensi produksi |
| `[project.optional-dependencies]` | Dependensi opsional (dev, test, docs) |
| `[project.scripts]` | Entry point untuk CLI (`pip install` bikin command) |
| `requires-python` | Versi Python minimal |


### Circular import — masalah dan solusi

**Masalah:** Module A import module B, dan module B import module A.
Terjadi `ImportError` karena salah satu module belum selesai di-load.

```python
# a.py
from b import fungsi_b   # error circular import
def fungsi_a(): ...

# b.py
from a import fungsi_a   # error circular import
def fungsi_b(): ...
```

**Solusi:**

1. **Restruktur kode** — pisahkan kode yang saling tergantung ke file ketiga (`common.py`)
2. **Lazy import** — import di dalam fungsi, bukan di atas file:
```python
# a.py
def fungsi_a():
    from b import fungsi_b  # import di sini, bukan di atas
    return fungsi_b()
```
3. **Gunakan `import module` bukan `from module import`**:
```python
# a.py
import b  # ini aman

def fungsi_a():
    return b.fungsi_b()
```


### Flat layout vs src layout

| Aspek | Flat layout | src layout (rekomendasi) |
|-------|-------------|-------------------------|
| Struktur | `my_project/main.py` | `src/my_project/main.py` |
| Kelebihan | Sederhana, akses langsung | Mencegah import langsung, testing lebih bersih |
| Kekurangan | Import ambigu, testing bisa salah | Sedikit lebih kompleks |
| Cocok untuk | Project kecil / single-file | Project menengah-besar / publik |

**Flat layout:**
```
my_project/
├── my_project.py
├── utils.py
├── tests/
│   └── test_my_project.py
```

**Src layout (rekomendasi):**
```
my_project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   └── test_my_project.py
├── pyproject.toml
└── README.md
```


### Best practices

1. **Gunakan src layout** untuk proyek yang akan dibagikan atau di-publish
2. **`__init__.py` minimalis** — hanya untuk re-export atau inisialisasi
3. **Gunakan absolute import** di aplikasi, relative import hanya di dalam package yang sama
4. **Satu modul = satu tanggung jawab** — jangan buat file terlalu besar
5. **Hindari circular import** sejak awal dengan perencanaan struktur yang baik
6. **Gunakan `pip install -e .`** saat development, jangan andalkan `sys.path`
7. **Tulis `pyproject.toml`** meskipun proyek kecil — memudahkan instalasi dan distribusi
8. **Naming convention:**
   - Package: huruf kecil, tanpa underscore jika memungkinkan (`myproject`)
   - Module: huruf kecil, dengan underscore jika perlu (`my_module.py`)
9. **Tes di `tests/`** — mirror struktur `src/` untuk memudahkan navigasi
10. **Dokumentasi** minimal README.md + docstring di fungsi/class penting


