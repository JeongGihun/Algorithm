def solution(numbers):
    answer = []
    n_list = []
    for i in numbers :
        if i % 2 == 0 :
            answer.append(i+1)
        else :
            tmp = bin(i)[2:]
            idx = tmp.rfind("0")
            if idx == -1 :
                num = "10" + tmp[idx+2:]
            else:
                num = tmp[:idx] + "10" + tmp[idx+2:]
            answer.append(int(num, 2))
            
    return answer