def solution(num_list):
    answer = []
    l = len(num_list)
    tmp = 0
    for num in num_list :
        if num % 2 == 0 :
            tmp += 1
    return [tmp, l-tmp]