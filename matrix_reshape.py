a = [[1,2,3,4],[5,6,7,8]]

new_shape = (4,2)

print(len(a))

one_d = []
for i in range(len(a)):
    for j in range(len(a[0])):
        one_d.append(a[i][j])
    print(f"one_d : {one_d}")
new_matrix =[]
x=0
for i in range(new_shape[0]):
    row = []
    for j in range(new_shape[1]):
        row.append(one_d[x])
        x+=1
    print(f"row : {row}")
    new_matrix.append(row)

print(f"new matrix ; {new_matrix}")


import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    arr = np.array(a)

    if arr.size != new_shape[0] * new_shape[1]:
        return []
    reshaped_matrix = arr.reshape(new_shape).tolist()
    return reshaped_matrix

