import numpy as np

list1 = [1, 2, 3]
list2 = [4, 5.0, 6]

a, b = np.array(list1), np.array(list2)

c = a + b
d = a - b
e = a * b
f = a / b
g = a * 2
h = b + 2


print("a자료형", type(a), type(a[0]))
print("b자료형", type(b), type(b[0]))
print("c자료형", type(c), type(c[0]))
print("d자료형", type(d), type(d[0]))
print("e자료형", type(e), type(e[0]))
print("f자료형", type(f), type(f[0]))
print("g자료형", type(g), type(g[0]))
print("h자료형", type(h), type(h[0]))

print(c,d,e)