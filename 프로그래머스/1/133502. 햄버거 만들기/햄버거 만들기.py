def solution(ingredient):
    answer = 0
    l = len(ingredient)
    stack = []
    for i in range(l) :
        stack.append(ingredient[i])
        while len(stack) > 3 and stack[-4:] == [1, 2, 3, 1] :
            for _ in range(4) :
                stack.pop()
            answer += 1
    return answer