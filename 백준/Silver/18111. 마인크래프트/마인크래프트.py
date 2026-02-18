import sys
from collections import Counter
input = sys.stdin.readline

n, m, p = map(int, input().split())
graph = []
ans = []
for i in range(n) :
    graph.extend(list(map(int, input().split())))

# 카운팅
numbers = Counter(graph)

# 범위 구하기
max_, min_ = max(graph), min(graph)

# 시간 구하기
for height in range(min_, max_+1) :
    time = 0
    bag = p
    for number in numbers.keys() :
        # 파야하는 경우
        if height - number < 0 :
            time += (height - number) * numbers[number] * (-2)
            bag += (height - number) * numbers[number] * (-1)
        # 넣어야하는 경우
        else :
            time += (height - number) * numbers[number]
            bag -= (height - number) * numbers[number]
    if bag < 0 :
         continue
    ans.append([time, height])
ans.sort(key=lambda x : (x[0], -x[1]))
print(ans[0][0], ans[0][1])