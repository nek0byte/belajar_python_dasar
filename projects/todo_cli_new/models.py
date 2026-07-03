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
