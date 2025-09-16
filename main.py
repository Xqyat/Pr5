def find_negative_columns(matrix):
    n = len(matrix)
    m = len(matrix[0])
    negative_columns = []
    for col in range(m):
        if all(matrix[row][col] < 0 for row in range(n)):
            negative_columns.append(col)
    return negative_columns

matrix = [
    [-1.0, -2.5,  3.0],
    [-4.2, -0.1, -5.5],
    [-3.3, -6.7, -7.8]
]

print(find_negative_columns(matrix))  