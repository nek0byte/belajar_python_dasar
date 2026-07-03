# Loop
arr = [1, 2, 3, 4, 5]
print(arr)
print("for loop")
for x in arr:
    print(x)

print("for loop2")
for x in range(len(arr)):
    print(arr[x])

# While
print("while loop")
i = 1
while i < 6:
    print(i)
    print("hello")
    i += 1

# Do While
print("do while loop")
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break

# Nested Loop
print("nested loop")
arr = [1, 2, 3, 4, 5]
for x in arr:
    for y in arr:
        print(x, y)

# Nested While
print("nested while")
i = 1
while i < 6:
    j = 1
    while j < 6:
        print(i, j)
        j += 1
    i += 1

# Nested Do While
print("nested do while")
i = 1
while True:
    j = 1
    while True:
        print(i, j)
        j += 1
        if j > 5:
            break
    i += 1
    if i > 5:
        break

# function
print("function")
def my_function():
    print("Hello from a function")

my_function()

print("function with parameter")
def my_function1(fname):
    print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")

print("function with multiple parameter")
def my_function2(fname, lname):
    print(fname + " " + lname)

my_function2("Emil", "Refsnes")

print("function with variable number of arguments")
def my_function3(*kids):
    print("The youngest child is " + kids[2])

my_function3("Emil", "Tobias", "Linus")

print("function with variable number of keyword arguments")
def my_function4(**kid):
    print("His last name is " + kid["lname"])

my_function4(fname = "Tobias", lname = "Refsnes")

print("recursive function")
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
fac(5)


