'''
=== Mini ToDo List ===
-> Fitur Utama
1. Menambah task
2. Melihat task
3. Mengubah status task
4. Menghapus task

-> Semua task disimpan di list
kenapa list? karena list bisa diubah

-> Semua task direpresentasikan menggunakan dictionary
kenapa dictionary? karena data task punya format yang tetap
namun memiliki value yang beda beda

-> Fungsi tambah
1. meminta user input untuk task
2. membuat dictionary baru
3. memberikan ID otomatis berdasarkan jumlah task
4. menambah task ke list
5. menampilkan pesan berhasil
6. menampilkan daftar task

-> Fungsi lihat
1. mengecek apakah list kosong
2. jika kosong maka tampilkan pesan "kosong"
3. jika tidak kosong maka tampilkan daftar task

-> Fungsi update status
1. menampilkan daftar task
2. meminta user input untuk ID task
3. cari ID lalu ubah status

-> Fungsi hapus
1. menampilkan daftar task
2. meminta user input untuk ID task
3. cari ID lalu hapus
'''

tasks = []

def tambah_task():
    judul = input("Masukkan nama task: ")

    task = {
        "id": len(tasks) + 1,
        "judul": judul,
        "selesai": False
    }

    tasks.append(task)
    print('=============================')
    print("Task berhasil ditambahkan!")
    print('=============================')
    lihat_task()


def lihat_task():
    if not tasks:
        print("Belum ada task.")
        return

    print("Daftar Task:")

    for task in tasks:
        status = "Selesai" if task["selesai"] else "Belum selesai"

        print(
            f"{[task['id']]} | {task['judul']} - {status}"
        )

def update_task():
    if not tasks:
        print("Belum ada task.")
        return

    lihat_task()

    try:
        id_task = int(input("\nMasukkan ID task yang ingin di update: "))

        for task in tasks:
            if task["id"] == id_task:
                task["selesai"] = True
                print("Task berhasil diupdate")
                lihat_task()
                return

    except ValueError:
        print("Masukkan angka yang valid")



def hapus_task():
    if not tasks:
        print("Belum ada task untuk dihapus.")
        return

    lihat_task()

    try:
        id_task = int(input("\nMasukkan ID task yang ingin dihapus: "))

        for task in tasks:
            if task["id"] == id_task:
                tasks.remove(task)
                print("Task berhasil dihapus!")
                return

        print("Task tidak ditemukan.")

    except ValueError:
        print("Masukkan angka yang valid.")


def tampilkan_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Tambah Task")
    print("2. Lihat Task")
    print("3. Hapus Task")
    print("4. Update Task")
    print("5. Keluar")


def main():
    while True:
        tampilkan_menu()

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_task()

        elif pilihan == "2":
            lihat_task()

        elif pilihan == "3":
            hapus_task()

        elif pilihan == "4":
            update_task()

        elif pilihan == "5":
            print("Program berakhir")
            break

        else:
            print("Pilihan tidak tersedia.")

main()
