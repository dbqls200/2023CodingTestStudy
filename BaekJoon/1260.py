#

from collections import deque

n, m, v = map(int, input().split())

graph = [[]]
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [False] * (n + 1)

def dfs(graph, v, visited):
    visited[v] = True

    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, v, visited)

print(graph)
