t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    matrix = [[0 for j in range(m)] for i in range(n)]
    
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            matrix[i][j] = row[j]
            
    v = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                v.append((i, j))
                
    for i in range(len(v)):
        k, j = v[i][0], v[i][1]
        for h in range(m):
            matrix[k][h] = 0
            
        for h in range(n - 1, -1, -1):
            matrix[h][j] = 0
            
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=' ')
        print()
