from collections import deque
def solution(n, wires):
    # 그래프 생성
    ans = []
    
    # 함수 생성
    def dfs(node) :
        chk = 1
        visit[node] = True
        go = deque([node])
        while go :
            tmp = go.pop()
            for i in graph[tmp] :
                if not visit[i] :
                    chk += 1
                    visit[i] = True
                    go.append(i)
        return chk               
    
    for i in range(len(wires)) :
        graph = {k:[] for k in range(1, n+1)}
        visit = {k:False for k in range(1, n+1)}
        for j in range(len(wires)) :
            if i != j :
                w1, w2 = wires[j]
                graph[w1].append(w2)
                graph[w2].append(w1)
        num = dfs(1)
        ans.append(abs(n-2*num))    
            
    return min(ans)