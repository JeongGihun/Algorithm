def solution(sizes):
    answer = 0
    
    for i in range(len(sizes)) :
        if sizes[i][0] < sizes[i][1] :
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    list_x = list(map(lambda x: x[0], sizes))
    list_y = list(map(lambda x: x[1], sizes))
    
    answer = max(list_x) * max(list_y)
    return answer