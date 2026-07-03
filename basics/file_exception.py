# file handling
student_file = open("student.txt", "w")
student_file.write("hello world")
student_file.close()

student_file = open("student.txt", "r")
print(student_file.read())
student_file.close()

# exception handling
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
    student_file.write("ohayo sekai") # timpa hello world 
    student_file.close()
except FileNotFoundError:
    print("file not found")


# delete file
import os
try:
    os.remove("student.txt")
except FileNotFoundError:
   print("file not found")


