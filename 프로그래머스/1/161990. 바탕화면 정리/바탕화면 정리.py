def solution(wallpaper):
    answer = []
    check = []
    x, y = len(wallpaper[0]), len(wallpaper)
    for j in range(y) :
        for i in range(x) :
            if wallpaper[j][i] == "#" :
                check.append([j, i])
                
    fun_x = [check[i][0] for i in range(len(check))]
    fun_y = [check[i][1] for i in range(len(check))]
    return [min(fun_x), min(fun_y), max(fun_x)+1, max(fun_y)+1]