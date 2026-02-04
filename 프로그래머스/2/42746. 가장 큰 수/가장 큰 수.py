def solution(numbers):
    l = list(map(str, numbers))
    l.sort(key = lambda x : x*3, reverse=True)
    answer = ''.join(l)
    answer = str(int(answer))
    return answer