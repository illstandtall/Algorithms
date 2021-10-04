import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[False] * (n+1) for i in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    node, edge = map(int, sys.stdin.readline().split())
    graph[node][edge] = True
    graph[edge][node] = True


def dfs(vertex):
    if visited[vertex] is True:
        return
    print(vertex, end=' ')
    visited[vertex] = True
    for i in range(1, n+1):
        if graph[vertex][i] is True:
            dfs(i)


def bfs(vertex):
    queue = deque()
    queue.append(vertex)
    visited[vertex] = True
    while queue:
        vertex = queue[0]
        queue.popleft()
        print(vertex, end=' ')
        for i in range(1, n+1):
            if graph[vertex][i] is True:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True


dfs(v)
print()
visited = [False] * (n+1)
bfs(v)