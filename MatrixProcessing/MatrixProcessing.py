while True:
    while True:
        columns_and_row_a = list(input("A: \n"))
        columns_a = int(columns_and_row_a[0])
        row_a = int(columns_and_row_a[2])
        matrix_a = []
        row_true_a = 0
        for x in range(columns_a):
            matrix_a.append(list(map(int, input().split())))
        for height in range(len(matrix_a)):
            if len(matrix_a[height]) == row_a:
                row_true_a += 1
        if row_true_a == columns_a:
            break
        else:
            print("Please, try again")

    while True:
        columns_and_row_b = list(input("B: \n"))
        columns_b = int(columns_and_row_b[0])
        row_b = int(columns_and_row_b[2])
        matrix_b = []
        row_true_b = 0
        for x in range(columns_b):
            matrix_b.append(list(map(int, input().split())))
        for height in range(len(matrix_b)):
            if len(matrix_b[height]) == row_b:
                row_true_b += 1
        if row_true_b == columns_b:
            break
        else:
            print("Please, try again")

    if columns_a == columns_b and row_a == row_b:
        result = []
        for x in range(columns_a):
            result.append([0]*row_b)
        for x in range(len(matrix_a)):
            for y in range(len(matrix_a[0])):
                result[x][y] = matrix_a[x][y] + matrix_b[x][y]
        for matrix_result in range(len(result)):
            print(*result[matrix_result])
            break
    else:
        print("ERROR")
