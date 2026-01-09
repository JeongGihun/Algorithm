from collections import deque
import sys
input = sys.stdin.readline

num = int(input())
graph = [[] for i in range(num+1)]
parent_node = [0 for _ in range(num+1)]  # 부모 노드
visit = [False for _ in range(num+1)]
visit[0] = True
q = deque([[1, 0]])

for i in range(num-1) :
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

while q :
    c, p = q.popleft()
    if c != 1 :
        parent_node[c] = p
    visit[c] = True
    for i in graph[c] :
        if not visit[i] :
            q.append([i, c])
            parent_node[i] = c
            visit[i] = True
parent_node = parent_node[2:]

for ans in parent_node :
    print(ans)