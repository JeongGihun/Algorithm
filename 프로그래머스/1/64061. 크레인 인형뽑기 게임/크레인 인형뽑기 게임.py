def solution(board, moves):
    answer = 0
    stack = []
    check = []
    
    for i in range(len(moves)) :
        moves[i] -= 1
        for j in range(len(board[0])) :
            if board[j][moves[i]] != 0 :
                stack.append(board[j][moves[i]])
                board[j][moves[i]] = 0
                break
    
    while stack :
        if not check :
            check.append(stack.pop())
        elif check[-1] == stack[-1] :
            check.pop()
            stack.pop()
            answer += 2
        else :
            check.append(stack.pop())
    
    return answer