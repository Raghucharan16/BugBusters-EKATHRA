t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    v = []
    rmin, rmax, colmin, colmax = 0, m - 1, 0, n - 1
    while rmin <= rmax and colmin <= colmax:
        for i in range(colmin, colmax + 1):
            v.append(matrix[rmin][i])
        rmin += 1
        for i in range(rmin, rmax + 1):
            v.append(matrix[i][colmax])
        colmax -= 1
        if rmin <= rmax:
            for i in range(colmax, colmin - 1, -1):
                v.append(matrix[rmax][i])
            rmax -= 1
        if colmin <= colmax:
            for i in range(rmax, rmin - 1, -1):
                v.append(matrix[i][colmin])
            colmin += 1
    for i in v:
        print(i, end=" ")
    print()
