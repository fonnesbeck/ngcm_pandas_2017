import numpy as np

X = np.arange(1, 16).reshape(5, 3, order='F')
print(X)

Y = X[[1, 3]]
print(Y)
