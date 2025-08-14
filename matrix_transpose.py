import time 

def transpose_matrix1(matrix):
    if not matrix :
        print('Matrix is empty')
        return []
    else:
        transpose_matrix = []
        for i in range(len(matrix[0])):
            new_row = []
            for row in matrix :
                new_row.append(row[i])
            transpose_matrix.append(new_row)
        return transpose_matrix

def transpose_matrix2(matrix):
    if not matrix :
        print('Matrix is empty')
        return []
    else:
        return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6]]
    # Record start time
    start_time = time.time()
    print(f"Function started at: {time.strftime('%H:%M:%S', time.localtime(start_time))}\n")
    
    transpose_matrix = transpose_matrix1(matrix)
    # Record start time
    end_time = time.time()
    print(f"Function end at: {time.strftime('%H:%M:%S', time.localtime(end_time))}\n")
    
    print(f"the transpose matrix is {transpose_matrix}")

    # Record start time
    start_time = time.time()
    print(f"Function started at: {time.strftime('%H:%M:%S', time.localtime(start_time))}\n")
    
    transpose_matrix = transpose_matrix2(matrix)
    # Record start time
    end_time = time.time()
    print(f"Function end at: {time.strftime('%H:%M:%S', time.localtime(end_time))}\n")
    
    print(f"the transpose matrix is {transpose_matrix}")