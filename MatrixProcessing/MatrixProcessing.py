import ast
import itertools
from math import floor, ceil


def mxinpt(row):
    line = row
    array = []
    for x in range(line):
        t = []
        for y in input().split():
            if y != " ":
                t.append(ast.literal_eval(y))
        array.append(t)
    return array


def mxp(result, row, column):
    line, columns = row, column
    for x in range(line):
        for y in range(columns):
            if result[x][y] == -0.0:
                print(0, end=" ")
            elif type(result[x][y]) == int or result[x][y] == 0:
                print(result[x][y], end=" ")
            elif type(result[x][y]) == float and result[x][y] != 0:
                if result[x][y] > 0:
                    print(floor(result[x][y]* 100) / 100.0, end=" ")
                else:
                    print(ceil(result[x][y] * 100) / 100.0, end=" ")

        print()


def mxsum(m1, m2, row, col):
    line, columns = row, col
    append = []
    for x in range(line):
        temp = []
        for y in range(columns):
            temp.append(m1[x][y] + m2[x][y])
        append.append(temp)
    return append


def mxnmbmtply(m1, number_m):
    multiply = []
    for x in range(len(a)):
        temp = []
        for y in range(len(a[0])):
            temp.append(m1[x][y] * number_m)
        multiply.append(temp)
    return multiply


def mxelsum(l1, l2):
    result = 0
    for x in range(len(l1)):
        result += l1[x] * l2[x]
    return result


def mx2mtpl(m1, m2):
    value = [[0 for row in range(len(m2[0]))] for column in range(len(m1))]
    for x in range(len(m1)):
        l1 = m1[x]
        for y in range(len(m2[0])):
            l2 = [m2[x][y] for x in range(len(m2))]
            value_range = mxelsum(l1, l2)
            value[x][y] = value_range
    return value


def trps_main_dg(array):
    return list(itertools.zip_longest(*array))


def trps_side_dg(array):
    new_matrix = [[array[y][x] for y in range(len(array))] for x in range(len(array[0]) - 1, -1, -1)]
    result = []
    for x in range(len(new_matrix[0])):
        new_matrix[x] = new_matrix[x][::-1]
        result.append(new_matrix[x])
    return result


def trps_vrt_line(array):
    new_matrix = [[array[y][x] for y in range(len(array))] for x in range(len(array[0]) - 1, -1, -1)]
    result = list(itertools.zip_longest(*new_matrix))
    return result


def trps_hrt_line(array):
    result = list(itertools.zip_longest(*array[::-1]))
    result = list(itertools.zip_longest(*result))
    return result


def minor(matrix_minor, x, y):
    return [row[:y] + row[y+1:] for row in (matrix_minor[:x] + matrix_minor[x + 1:])]


def minor_trps(array):
    determinant = det(array)
    if len(array) == 2:
        return [[array[1][1] / determinant, -1 * array[0][1] / determinant],
                [-1 * array[1][0] / determinant, array[0][0] / determinant]]
    cofactors = []
    for z in range(len(array)):
        case = []
        for y in range(len(array)):
            minored = minor(array, z, y)
            case.append(((-1)**(z+y)) * det(minored))
        cofactors.append(case)
    cofactors = trps_main_dg(cofactors)
    for x in range(len(cofactors)):
        cofactors[x] = list(cofactors[x])
    for z in range(len(cofactors)):
        for y in range(len(cofactors)):
            cofactors[z][y] = int(cofactors[z][y]) / determinant
    return cofactors


def det(matrix_det):
    if len(matrix_det) == 2:
        return matrix_det[0][0] * matrix_det[1][1] - matrix_det[0][1] * matrix_det[1][0]
    determinant = 0
    for x in range(len(matrix_det)):
        determinant += ((-1) ** x) * matrix_det[0][x] * det(minor(matrix_det, 0, x))
    return determinant


while True:
    action = str(input("let's begin: yes or no? "))
    if action == "yes":
        print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
        choice = int(input("Your choice:"))
        if choice == 1:
            matrix, n = map(int, input("Enter size of first matrix:").split())
            print("Enter first matrix:")
            a = mxinpt(matrix)
            p, q = map(int, input("Enter size of second matrix:").split())
            print("Enter second matrix:")
            b = mxinpt(p)
            if matrix != p and n != q:
                print("The operation cannot be performed.")
            else:
                c = mxsum(a, b, matrix, n)
                mxp(c, matrix, n)
        elif choice == 2:
            matrix, n = map(int, input("Enter size of matrix:").split())
            print("Enter matrix:")
            a = mxinpt(matrix)
            number = float(input("Enter constant:"))
            c = mxnmbmtply(a, number)
            print("The result is:")
            mxp(c, matrix, n)
        elif choice == 3:
            matrix, n = map(int, input("Enter size of first matrix:").split())
            print("Enter first matrix:")
            a = mxinpt(matrix)
            p, q = map(int, input("Enter size of second matrix:").split())
            print("Enter second matrix:")
            b = mxinpt(p)
            c = mx2mtpl(a, b)
            print("The result is:")
            mxp(c, matrix, q)
        elif choice == 4:
            print("""1. Main diagonal
        2. Side diagonal
        3. Vertical line
        4. Horizontal line.""")
            choice = int(input("Your choice:"))
            if choice == 1:
                matrix, n = map(int, input("Enter size of matrix:").split())
                print('Enter matrix:')
                a = mxinpt(matrix)
                c = trps_main_dg(a)
                print('The result is:')
                mxp(c, n, matrix)
            elif choice == 2:
                matrix, n = map(int, input("Enter size of matrix:").split())
                print('Enter matrix:')
                a = mxinpt(matrix)
                c = trps_side_dg(a)
                print('The result is:')
                mxp(c, n, matrix)
            elif choice == 3:
                matrix, n = map(int, input("Enter size of matrix:").split())
                print('Enter matrix:')
                a = mxinpt(matrix)
                c = trps_vrt_line(a)
                print('The result is:')
                mxp(c, matrix, n)
            elif choice == 4:
                matrix, n = map(int, input("Enter size of matrix:").split())
                print('Enter matrix:')
                a = mxinpt(matrix)
                c = trps_hrt_line(a)
                print('The result is:')
                mxp(c, matrix, n)
        elif choice == 5:
            matrix, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = mxinpt(matrix)
            c = det(a)
            print('The result is:')
            print(c)
        elif choice == 6:
            matrix, n = map(int, input("Enter size of matrix:").split())
            print('Enter matrix:')
            a = mxinpt(matrix)
            c = det(a)
            print(c)
            if c != 0:
                d = minor_trps(a)
                print('The result is:')
                mxp(d, matrix, n)
            else:
                print("This matrix doesn't have an inverse.")
        elif choice == 0:
            break
        action = str(input("Shall we continue: yes or no? "))
        if action == "yes":
            continue
        elif action == "no":
            break
        else:
            print("Incorrect input")
    elif action == "no":
        break
    else:
        print("Incorrect input")