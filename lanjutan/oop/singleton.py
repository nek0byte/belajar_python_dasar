"""
SINGLETON PATTERN

Singleton adalah design pattern yang memastikan sebuah class hanya
memiliki SATU instance sepanjang program berjalan. Berguna untuk
resource global seperti koneksi database, logger, atau konfigurasi.
"""

"""
1. Via __new__: pendekatan paling umum
Override method __new__ untuk mengontrol pembuatan instance.
"""


class SingletonNew:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


a = SingletonNew()
b = SingletonNew()
print(a is b)  # True
print(id(a) == id(b))  # True


"""
2. Via __new__ dengan inisialisasi sekali
__init__ dipanggil setiap kali, jadi perlu guard agar hanya jalan sekali.
"""


class SingletonInit:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, nama=""):
        if not self._initialized:
            self.nama = nama
            type(self)._initialized = True


s1 = SingletonInit("Versi 1")
s2 = SingletonInit("Versi 2")
print(s1.nama)  # Versi 1 (inisialisasi hanya sekali)
print(s1 is s2)  # True


"""
3. Via Metaclass: reusable untuk banyak class
Metaclass mengontrol pembuatan instance via __call__.
"""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.data = {}


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.logs = []


c1 = Config()
c2 = Config()
print(c1 is c2)  # True

l1 = Logger()
l2 = Logger()
print(l1 is l2)  # True (metaclass bekerja untuk class berbeda)


"""
4. Module as Singleton: cara paling Pythonic
Python hanya mengeksekusi module SEKALI saat pertama di-import.
Instance di level module otomatis menjadi singleton.
"""


# Cukup buat instance di level module:
class Database:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True


db = Database()  # instance dibuat sekali

# Di file lain cukup: from singleton import db
# Variabel `db` adalah instance yang sama karena module di-cache.


"""
5. Decorator Singleton: tanpa mengubah class asli
Decorator membungkus class sehingga hanya membuat satu instance.
"""


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Cache:
    def __init__(self):
        self.data = {}


cache1 = Cache()
cache2 = Cache()
print(cache1 is cache2)  # True


"""
6. Borg Pattern (Monostate): shared state, beda instance
Semua instance berbagi __dict__ yang sama, jadi state selalu sinkron.
"""


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


b1 = Borg()
b1.x = 10

b2 = Borg()
b2.y = 20

print(b1.x)  # 10
print(b2.x)  # 10 (state sama)
print(b1.y)  # 20
print(b1 is b2)  # False (instance berbeda)


"""
7. Thread-safe Singleton: aman untuk multi-threading
Gunakan threading.Lock agar tidak ada race condition.
"""

import threading


class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance


ts1 = ThreadSafeSingleton()
ts2 = ThreadSafeSingleton()
print(ts1 is ts2)  # True


"""
8. Contoh real-world: ConfigManager
Menyimpan konfigurasi global yang bisa diakses dari mana saja.
"""


class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._config = {}
        return cls._instance

    def set(self, key, value):
        self._config[key] = value

    def get(self, key, default=None):
        return self._config.get(key, default)

    def semua(self):
        return self._config


cfg1 = ConfigManager()
cfg1.set("version", "2.0.0")
cfg1.set("debug", True)

cfg2 = ConfigManager()
cfg2.set("app_name", "TodoApp")

print(cfg1.get("version"))  # 2.0.0
print(cfg2.get("version"))  # 2.0.0
print(cfg1.get("app_name"))  # TodoApp
print(cfg1 is cfg2)  # True


"""
9. Perbandingan metode Singleton

| Metode       | Cocok untuk              | Kelebihan                  | Kekurangan                  |
|-------------|--------------------------|----------------------------|-----------------------------|
| __new__     | Class tunggal            | Sederhana, mudah dibaca    | Tidak reusable             |
| Metaclass   | Banyak class             | Reusable, fleksibel        | Complex, overhead          |
| Decorator   | Class apa pun            | Tidak ubah class asli      | Hasil bukan class asli     |
| Module      | Konstanta / koneksi      | Paling Pythonic, built-in  | Tidak bisa lazy init       |
| Borg        | Butuh shared state       | Instance tetap beda        | Bukan singleton murni      |
| thread-safe | Multi-threading          | Aman concurrent            | Overhead lock              |
"""

if __name__ == "__main__":
    print("\nDemo singleton selesai.")
