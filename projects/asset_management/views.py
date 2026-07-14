def input_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input harus berupa angka.")


def input_kode() -> str:
    return input("Kode: ")


def input_int_opsi(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        pilih = input_int(prompt)
        if min_val <= pilih <= max_val:
            return pilih
        print(f"Pilih {min_val}-{max_val}.")


def tampilkan_menu_utama() -> None:
    print("\n1. Tambah Aset")
    print("2. Lihat Daftar Aset")
    print("3. Keluar")


def tampilkan_menu_tambah() -> None:
    print("\n1. Tambah Kendaraan")
    print("2. Tambah Elektronik")
    print("3. Tambah Tanah Bangunan")
    print("4. Kembali")


def tampilkan_menu_setelah_lihat() -> None:
    print("\nMenu")
    print("1. Ubah Aset")
    print("2. Hapus Aset")
    print("3. Kembali")


def input_aset_kendaraan() -> tuple[str, str, int, str, int]:
    print("\nTambah Kendaraan")
    kode = input_kode()
    nama = input("Nama: ")
    harga = input_int("Harga: ")
    stkn = input("STKN: ")
    tahun = input_int("Tahun: ")
    return kode, nama, harga, stkn, tahun


def input_aset_elektronik() -> tuple[str, str, int, str]:
    print("\nTambah Elektronik")
    kode = input_kode()
    nama = input("Nama: ")
    harga = input_int("Harga: ")
    serial_number = input("Serial Number: ")
    return kode, nama, harga, serial_number


def input_aset_tanah_bangunan() -> tuple[str, str, int, str, int, int]:
    print("\nTambah Tanah Bangunan")
    kode = input_kode()
    nama = input("Nama: ")
    harga = input_int("Harga: ")
    sertifikat = input("Sertifikat: ")
    njop = input_int("NJOP: ")
    luas = input_int("Luas: ")
    return kode, nama, harga, sertifikat, njop, luas


def input_data_ubah_kendaraan() -> tuple[str, int, str, int]:
    nama = input("Nama: ")
    harga = input_int("Harga: ")
    stkn = input("STKN: ")
    tahun = input_int("Tahun: ")
    return nama, harga, stkn, tahun


def input_data_ubah_elektronik() -> tuple[str, int, str]:
    nama = input("Nama: ")
    harga = input_int("Harga: ")
    serial_number = input("Serial Number: ")
    return nama, harga, serial_number


def input_data_ubah_tanah_bangunan() -> tuple[str, int, str, int, int]:
    nama = input("Nama: ")
    harga = input_int("Harga: ")
    sertifikat = input("Sertifikat: ")
    njop = input_int("NJOP: ")
    luas = input_int("Luas: ")
    return nama, harga, sertifikat, njop, luas


def tampilkan_aset_kendaraan(aset) -> None:
    print("\nAset Kendaraan")
    print("Kode:", aset.kode)
    print("Nama:", aset.nama)
    print("Harga:", aset.harga)
    print("STKN:", aset.stkn)
    print("Tahun:", aset.tahun)


def tampilkan_aset_elektronik(aset) -> None:
    print("\nAset Elektronik")
    print("Kode:", aset.kode)
    print("Nama:", aset.nama)
    print("Harga:", aset.harga)
    print("Serial Number:", aset.serial_number)


def tampilkan_aset_tanah_bangunan(aset) -> None:
    print("\nAset Tanah Bangunan")
    print("Kode:", aset.kode)
    print("Nama:", aset.nama)
    print("Harga:", aset.harga)
    print("Sertifikat:", aset.sertifikat)
    print("NJOP:", aset.njop)
    print("Luas:", aset.luas)


def tampilkan_pesan(teks: str) -> None:
    print(teks)
