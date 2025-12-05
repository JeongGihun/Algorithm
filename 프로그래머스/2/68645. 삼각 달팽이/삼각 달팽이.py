def solution(n):
    answer = [[0 for j in range(i+1)] for i in range(n)]
    dir = [[0, 1], [1, 0], [-1, -1]]
    num = 0
    x, y = 0, -1
    for i in range(n) :
        dx, dy = dir[i%3][0], dir[i%3][1]
        for j in range(n-i) :
            x, y = x+dx, y+dy
            num += 1
            answer[y][x] = num
    result = []
    for i in answer :
        result += i
    return result