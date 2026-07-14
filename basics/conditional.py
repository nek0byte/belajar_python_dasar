# conditional statements
a = 10
b = 20

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# ternary operator
a = 10
b = 20
print("a is greater than b") if a > b else print("a is less than b")

# short circuiting
a = 10
b = 20
c = 30
print("a is greater than b and c") if a > b and a > c else print(
    "a is less than b or c")

# nested if
a = 10
b = 20
c = 30
if a > b:
    if a > c:
        print("a is greater than b and c")
    else:
        print("a is greater than b but less than c")
else:
    print("a is less than b")
