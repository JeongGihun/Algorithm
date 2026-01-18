def solution(k, score):
    answer = []
    stack = []
    for i in range(len(score)) :
        stack.append(score[i])
        stack.sort(reverse=True)
        if len(stack) > k :
            stack.pop()
        answer.append(min(stack))
    return answer