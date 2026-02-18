def solution(a, b):
    answer1 = str(a)+str(b)
    answer3 = 2*a*b
    print(int(answer1), answer3)
    return max(int(answer1), answer3)