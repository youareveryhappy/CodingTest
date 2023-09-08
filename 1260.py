from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().split())

graph = [[0]*(n+1) for _ in range(n+1)]
print(graph)

visit_list = [0] * (n+1)
visit_list2 = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

print(graph)