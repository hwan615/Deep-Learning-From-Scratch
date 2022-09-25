import numpy as np

def printDimInfo(x):
    print("target", x)
    print("dimension", np.ndim(x))
    print("shape", x.shape)

# 1차원
dim1 = np.array([1, 2, 3, 4])
printDimInfo(dim1)

# 2차원
dim2 = np.array([[1,2], [2,3], [3,4]])
printDimInfo(dim2)

# 3차원
dim3 = np.array([[[1,2,3],[3,4,5]], [[1,2,5], [2,4,5]]])
printDimInfo(dim3)