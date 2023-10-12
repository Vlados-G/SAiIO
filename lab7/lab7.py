def try_kuhn(v):
    if used[v]:
        return False
    used[v] = True
    for to in g[v]:
        if mt[to] == -1 or try_kuhn(mt[to]):
            mt[to] = v
            return True
    return False


# Задайте матрицу смежности
adjacency_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

n = len(adjacency_matrix)  # Количество вершин в левой доле
k = len(adjacency_matrix[0])  # Количество вершин в правой доле

g = [[] for _ in range(n)]

for i in range(n):
    for j in range(k):
        if adjacency_matrix[i][j] == 1:
            g[i].append(j)

mt = [-1] * k
used1 = [False] * n

for i in range(n):
    for j in g[i]:
        if mt[j] == -1:
            mt[j] = i
            used1[i] = True
            break

for i in range(n):
    if used1[i]:
        continue
    used = [False] * n
    try_kuhn(i)

# Вывод паросочетания
for i in range(k):
    if mt[i] != -1:
        print(mt[i] + 1, i + 1)
