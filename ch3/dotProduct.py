import numpy as np

x = np.array([1,2])
print(x.shape)
y = np.array([[1,2], [2,4]])
print(y.shape)

result = np.dot(x,y)
print(result)