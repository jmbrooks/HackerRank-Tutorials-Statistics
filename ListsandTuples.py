tup1 = 2, 3, 5, 7
list1 = [2, 6, 5]

print(tup1)
print(list1)

tup2 = 2, 'meep', True

print(tup2)
list1.append(10)
print(list1)

print(list1.insert(3, 1))
list1.remove(6)
print(list1)

print(list1[0])
print(list1.index(5))
print(list1.count(5))
list1.sort()
print(list1)

y = ['Jan', 'Dan', 'Bob', 'Alice', 'Jon', 'Jack']
y.sort()
print(y)
y.reverse()
print(y)

z = [[3, 2], [4, 5], [6, 7]]
print(z)
print(z[0])
print(z[0][0])

z1 = [
    [5, 2],
    [6, 2],
    [3, 1],
    [12, 6]
    ]
print(z1)
z1.pop()
