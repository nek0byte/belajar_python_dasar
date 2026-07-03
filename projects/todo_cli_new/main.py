import task_manager

def tampilkan_menu():

    print("""
====================
      TODO APP
====================

1. Tambah Task
2. Lihat Task
3. Cari Task
4. Edit Task
5. Tandai Selesai
6. Hapus Task
7. Keluar

""")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul = input("Nama task: ")
            task_manager.tambah_task(judul)
            print("Task berhasil ditambahkan")
            task_manager.lihat_task()

        elif pilihan == "2":
            tasks = task_manager.lihat_task()
            if not tasks:
                print("Belum ada task")
            else:
                for task in tasks:
                    print(task)

        elif pilihan == "3":
            keyword = input("Cari: ")
            hasil = task_manager.cari_task(keyword)
            for task in hasil:
                print(task)

        elif pilihan == "4":
            id_task = int(
                input("ID task: ")
            )

            judul = input(
                "Judul baru: "
            )

            berhasil = task_manager.edit_task(
                id_task,
                judul
            )

            print(
                "Berhasil"
                if berhasil
                else "Task tidak ditemukan"
            )

        elif pilihan == "5":
            id_task = int(
                input("ID task selesai: ")
            )
            berhasil = task_manager.selesai_task(
                id_task
            )
            print(
                "Berhasil"
                if berhasil
                else "Task tidak ditemukan"
            )

        elif pilihan == "6":
            id_task = int(
                input("ID task hapus: ")
            )
            berhasil = task_manager.hapus_task(
                id_task
            )
            print(
                "Berhasil"
                if berhasil
                else "Task tidak ditemukan"
            )

        elif pilihan == "7":
            print("Sampai jumpa!")
            break

        else:
            print("Menu tidak tersedia")


if __name__ == "__main__":
    main()
