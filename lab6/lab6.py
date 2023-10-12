import itertools
import math
import networkx as nx
import matplotlib.pyplot as plt


def tsp_bellman_held_karp(C):
    n = len(C)
    all_nodes = set(range(1, n + 1))  # Изменили нумерацию вершин

    # Инициализация dp массива
    dp = {}

    # Заполняем dp[(frozenset({i}), i)] для всех i
    for i in range(1, n):
        dp[(frozenset({i}), i)] = C[i - 1][0]  # Изменили индексацию матрицы

    # Динамическое программирование
    for size in range(2, n):
        for subset in itertools.combinations(all_nodes - {1}, size):  # Изменили нумерацию вершин
            subset = frozenset(subset)
            for k in subset:
                if k != 1:  # Избегаем обработки случаев с k == 1
                    dp[(subset, k)] = min(C[k - 1][j - 1] + dp.get((subset - {k}, j), math.inf) for j in subset if
                                          j != k)  # Изменили индексацию матрицы и обработку отсутствующих значений

    # Вычисляем минимальное расстояние и восстанавливаем путь
    subset = frozenset(all_nodes - {1})  # Изменили нумерацию вершин
    min_distance = min(C[k - 1][0] + dp.get((subset, k), math.inf) for k in
                       subset)  # Изменили индексацию матрицы и обработку отсутствующих значений

    path = [1]  # Изменили начальную вершину
    last_node = 1  # Изменили начальную вершину
    while len(path) < n:
        next_node = min((j for j in all_nodes if j != last_node and (subset - {last_node}) & {j}),
                        key=lambda j: C[last_node - 1][j - 1] + dp.get((subset - {last_node}, j),
                                                                       math.inf))  # Изменили индексацию матрицы и обработку отсутствующих значений
        path.append(next_node)
        subset -= {last_node}
        last_node = next_node

    path.append(1)  # Изменили начальную вершину

    return min_distance, path


C = [
    [0, 1, 1, 7],
    [1, 0, 20, 1],
    [1, 20, 0, 1],
    [7, 1, 1, 0]
]

G = nx.Graph()

# Добавляем вершины в граф
n = len(C)
G.add_nodes_from(range(1, n + 1))  # Нумерация вершин начинается с 1

# Добавляем ребра с весами из матрицы C
for i in range(n):
    for j in range(n):
        if i != j:
            G.add_edge(i + 1, j + 1, weight=C[i][j])

# Построение графа
pos = nx.spring_layout(G)  # Расположение вершин
labels = nx.get_edge_attributes(G, 'weight')  # Веса ребер

nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Граф на основе матрицы расстояний C")
plt.axis('off')
plt.show()

min_distance, path = tsp_bellman_held_karp(C)
print("Минимальное расстояние:", min_distance)
print("Минимальный путь:", path)

