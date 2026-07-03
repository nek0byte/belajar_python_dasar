# variable & tipe data
# ====================
print('variabel & tipe data')
print('=====================')
a = 10
b = 'hello'
c = 3.14
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# type casting
a = float(10)
b = str('hello')
c = float(3.14)
d = bool(True)

# input & output
name = input('Masukkan nama: ')
print('Halo', name)

# operator
a = 10
b = 5
print('operator aritmatika')
print('=====================')
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

print('operator perbandingan')
print('=====================')
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

print('operator logika')
print('=====================')
# operator logika
print(a and b)
print(a or b)
print(not a)

print('operator bitwise')
print('=====================')
# operator bitwise
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << b)
print(a >> b)

print('operator assignment')
print('=====================')
# operator assignment
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a %= b
print(a)
a **= b
print(a)
a //= b
print(a)

print('operator bitwise assignment')
print('=====================')
# operator bitwise assignment
a, b = 10, 5
a &= b
print(a)
a |= b
print(a)
a ^= b
print(a)
a <<= b
print(a)
a >>= b
print(a)

print('operator membership')
print('=====================')
# operator membership
a = [1, 2, 3]
print(1 in a)
print(4 not in a)

print('operator identity')
print('=====================')
# operator identity
a = 10
b = 10
print(a is b)
print(a is not b)

print('operator ternary')
print('=====================')
# operator ternary
a = 10
b = 5
c = 3
print(a if a > b else b if b > c else c)

# struktur data
# ==============
print('struktur data')
print('==============')

# list
print('list')
a = [1, 2, 3]
print(a)
print(a[0])
print(a[1])
a[2] = 4
print(a[2])

# tuple
print('tuple')
a = (1, 2, 3)
print(a)
print(a[0])
print(a[1])
print(a[2])

# dictionary
# hashmap / hash table
print('dictionary')
a = {'name': 'John', 'age': 30}
print(a)
print(a['name'])
print(a['age'])

# set
print('set')
a = {1, 2, 3}
print(a)
print(1 in a)
print(4 not in a)

# string
print('string')
a = 'hello'
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

# slicing
print('slicing')
a = 'hello'
print(a[0:2]) 
print(a[2:4])
print(a[4:6])  

# string formatting
print('string formatting')
name = 'John'
age = 30
print('My name is %s and I am %d years old' % (name, age))
print('My name is {} and I am {} years old'.format(name, age))
print(f'My name is {name} and I am {age} years old')

# string methods
print('string methods')
a = 'hello world'
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.count('l'))
print(a.count(' '))
print(a.find('l'))
print(a.replace('l', 'L'))

# string operators
print('string operators')
a = 'hello'
b = 'world'
print(a + ' ' + b)
print(a * 3)
print('l' in a)
print('L' not in a)

# list methods
print('list methods')
a = [1, 2, 3]
print(a)
print("append")
a.append(4)
print(a)
print("insert")
a.insert(1, 2)
print(a)
print("remove")
a.remove(2)
print(a)
print("pop")
a.pop(0)
print(a)
print("index")
print(a.index(3))
print("count")
print(a.count(3))
print("sort")
a.sort()
print(a)
print("reverse")
a.reverse()
print(a)

# list operators
print('list operators')
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
print(3 in a)
print(4 not in a)

# tuple methods
print('tuple methods')
a = (1, 2, 3)
print(a)
print("count")
print(a.count(1))
print("index")
print(a.index(2))

# tuple operators
print('tuple operators')
a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)
print(a * 3)
print(3 in a)
print(4 not in a)

# set methods
print('set methods')
a = {1, 2, 3}
print(a)
print("copy")
print(a.copy())
print("add")
a.add(4)
print(a)
print("remove")
a.remove(2)
print(a)
print("pop")
a.pop()
print(a)

# set operators
print('set operators')
a = {1, 2, 3}
b = {4, 5, 6}
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

# dictionary methods
print('dictionary methods')
a = {'name': 'John', 'age': 30}
print(a)
print(a['name'])
print(a['age'])
print("keys")
print(a.keys())
print("values")
print(a.values())
print("items")
print(a.items())

'''
1. buat list acak trus urutin
2. tambah nilai baru di list
3. buat dictionary isinya nama, alamat, usia
'''
# rename
a['name'] = 'John Doe'
# add
a['address'] = 'Jalan Raya'
a['age'] = 30

list = [1, 2, 3, 4, 5]
list.sort()
print(list[-1])
