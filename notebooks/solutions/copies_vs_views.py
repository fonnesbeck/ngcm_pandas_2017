import numpy as np

a = np.arange(10)
a[2, 5] = 100
print(a)

a = np.arange(10)
b = a[2, 5]
b[:] = 100
print(a)
print(b)
