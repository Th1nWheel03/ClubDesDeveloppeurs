def SumOfMagicTriangle(size: int):

    array = [[0 for _ in range(size)] for _ in range(size)]

    for row in range(size):
        for col in range(row+1):
            if col == 0:
                array[row][col] = 1
            else:
                array[row][col] = array[row][col-1] + array[row-1][col]

    return array

triangle_size = 20
triangle = SumOfMagicTriangle(triangle_size)
sum = 0
for row in triangle[triangle_size-1]:
    sum+=row

print(f"Somme de la 20e ligne est : {sum}")