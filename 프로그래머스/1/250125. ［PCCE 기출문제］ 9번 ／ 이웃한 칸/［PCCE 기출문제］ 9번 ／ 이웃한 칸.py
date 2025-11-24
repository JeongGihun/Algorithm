def solution(board, h, w):
    answer = 0
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]
    check_color = board[h][w]
    for i in range(4) :
        if h+x[i] >=0 and w+y[i] >=0 and len(board[0])-1 >= h+x[i] and len(board)-1 >=w+y[i] :
            if board[h+x[i]][w+y[i]] == check_color :
                answer += 1
    
    return answer