import numpy as np
import timeit


def mat_access1(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            mat[i, j] *= 2


def mat_access2(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat.item(i, j)
            mat.itemset((i, j), k * 2)


def mat_access3(mat: np.ndarray):
    mat *= 2


mat1 = np.arange(100000000).reshape(200000, -1)
mat2 = np.arange(100000000).reshape(200000, -1)
mat3 = np.arange(100000000).reshape(200000, -1)

print("원소 처리 전: \n%s\n" % mat1)
start_time = timeit.default_timer()
mat_access1(mat1)
print(f"{round(timeit.default_timer() - start_time,15)}초 걸렸습니다.")
print("원소 처리 후: \n%s\n" % mat1)

print("원소 처리 전: \n%s\n" % mat2)
start_time = timeit.default_timer()
mat_access2(mat2)
print(f"{round(timeit.default_timer() - start_time,15)}초 걸렸습니다.")
print("원소 처리 후: \n%s" % mat2)

print("원소 처리 전: \n%s\n" % mat3)
start_time = timeit.default_timer()
mat_access3(mat3)
print(f"{round(timeit.default_timer() - start_time,15)}초 걸렸습니다.")
print("원소 처리 후: \n%s" % mat3)
