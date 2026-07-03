from models import Task

tasks = []

def generate_id():
    if not tasks:
        return 1

    return max(task.id for task in tasks) + 1

def tambah_task(judul):
    task = Task(
        generate_id(),
        judul
    )
    tasks.append(task)
    return task

def lihat_task():
    return tasks

def cari_task(keyword):
    hasil = []
    for task in tasks:
        if keyword.lower() in task.judul.lower():
            hasil.append(task)
    return hasil

def edit_task(id_task, judul_baru):
    for task in tasks:
        if task.id == id_task:
            task.judul = judul_baru
            return True
    return False

def selesai_task(id_task):
    for task in tasks:
        if task.id == id_task:
            task.tandai_selesai()
            return True
    return False


def hapus_task(id_task):
    for task in tasks:
        if task.id == id_task:
            tasks.remove(task)
            return True
    return False
