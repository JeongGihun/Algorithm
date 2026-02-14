from collections import deque

def solution(park, routes):
    answer = []
    dir = {'E' : (1, 0), 'S' : (0, 1), 'W' : (-1, 0), 'N' : (0, -1)}
    
    len_x, len_y = len(park[0]), len(park)
    loc = []
    # 시작 지점 찾기
    for y in range(len_y) :
        for x in range(len_x) :
            if park[y][x] == "S" :
                loc = [y, x]
                break
    
    # 이동
    for r in routes :
        go, check = r.split()
        nx, ny = loc[1], loc[0]
        
        for num in range(int(check)) :
            nx += dir[go][0]
            ny += dir[go][1]
            if nx < 0 or nx >= len_x or ny < 0 or ny >= len_y :
                break
            if park[ny][nx] == "X" :
                break
        else :
            loc = [ny, nx]
            

    return loc