import ast


def matrix_input(row):
    line = row
    matrix = []
    for x in range(line):
        t = []
        for y in input().split():
            if y != " ":
                t.append(ast.literal_eval(y))
        matrix.append(t)
    return matrix


def matrix_print(result, row, column):
    line, columns = row, column
    for x in range(line):
        for y in range(columns):
            print(result[x][y], end=' ')
        print()


def matrix_sum(m1, m2, row, col):
    line, columns = row, col
    append = []
    for x in range(line):
        temp = []
        for y in range(columns):
            temp.append(m1[x][y] + m2[x][y])
        append.append(temp)
    return append


def matrix_number_multiply(m1, number_m):
    multiply = []
    for x in range(len(a)):
        temp = []
        for y in range(len(a[0])):
            temp.append(float(m1[x][y]) * float(number_m))
        multiply.append(temp)
    return multiply


def matrix_element_sum(l1, l2):
    result = 0
    for x in range(len(l1)):
        result += l1[x] * l2[x]
    return result


def matrix_two_multiply(m1, m2):
    value = [[0 for row in range(len(m2[0]))] for column in range(len(m1))]
    print(value)
    for x in range(len(m1)):
        l1 = m1[x]
        for y in range(len(m2[0])):
            l2 = [m2[x][y] for i in range(len(m2))]
            value_range = matrix_element_sum(l1, l2)
            value[x][y] = value_range
    return value


while True:
    print('''
            1. Add matrices
            2. Multiply matrix by a constant
            3. Multiply matrices
            0. Exit
           ''', end='')
    choice = int(input('Your choice:'))
    if choice == 1:
        q, w = map(int, input('Enter size of first matrix:').split())
        print('Enter first matrix:')
        a = matrix_input(q)
        z, m = map(int, input('Enter size of second matrix:').split())
        print('Enter second matrix:')
        b = matrix_input(z)
        if m != z and w != m:
            print('The operation cannot be performed.')
        else:
            c = matrix_sum(a, b, q, w)
            matrix_print(c, q, w)
    elif choice == 2:
        m, n = map(int, input('Enter size of matrix:').split())
        print('Enter matrix:')
        a = matrix_input(m)
        number = float(input('Enter constant:'))
        c = matrix_number_multiply(a, number)
        print('The result is:')
        matrix_print(c, m, n)
    elif choice == 3:
        m, n = map(int, input('Enter size of first matrix:').split())
        print('Enter first matrix:')
        a = matrix_input(m)
        p, q = map(int, input('Enter size of second matrix:').split())
        print('Enter second matrix:')
        b = matrix_input(p)
        c = matrix_two_multiply(a, b)
        print('The result is:')
        matrix_print(c, m, q)
    elif choice == 0:
        break

