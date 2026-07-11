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
