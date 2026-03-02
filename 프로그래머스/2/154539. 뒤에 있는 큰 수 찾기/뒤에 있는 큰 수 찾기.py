def solution(numbers):
    answer = [-1 for i in numbers]
    stack = []
    for idx in range(len(numbers)) :
        while stack and stack[-1][0] < numbers[idx] :
            tmp = stack.pop()
            answer[tmp[1]] = numbers[idx]
        stack.append([numbers[idx],idx])
    return answer