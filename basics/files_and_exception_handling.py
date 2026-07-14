# file handling
student_file = open("student.txt", "w")
student_file.write("hello world")
student_file.close()

student_file = open("student.txt", "r")
print(student_file.read())
student_file.close()

# ========================================
# exception handling
"""
Exception / Error Handling adalah mekanisme untuk menangani error
yang terjadi saat program berjalan (runtime error).

-> Jika error tidak di-handle, program akan berhenti (crash).
-> Dengan try/except, kita bisa menangkap error dan memberi
   respon yang sesuai tanpa menghentikan program.

Struktur dasar:
    try:
        # kode yang berpotensi error
    except SomeError:
        # aksi jika error terjadi

Kita juga bisa menangkap beberapa jenis exception sekaligus,
misal: except (FileNotFoundError, PermissionError):
"""
try:
    student_file = open("studen.txt", "r")
    print(student_file.read())
    student_file.close()
except FileNotFoundError:
    print("file not found")

# update file
try:
    student_file = open("student.txt", "a")
    student_file.write("\nohayou sekai")
    student_file.close()
except FileNotFoundError:
    print("file not found")

try:
    student_file = open("student.txt", "r")
    print(student_file.read())
    student_file.close()
except FileNotFoundError:
    print("file not found")

# delete "hello world" text in file
try:
    student_file = open("student.txt", "w")
    student_file.write("ohayo sekai")  # timpa hello world
    student_file.close()
except FileNotFoundError:
    print("file not found")


# delete file
import os

try:
    os.remove("student.txt")
except FileNotFoundError:
    print("file not found")
