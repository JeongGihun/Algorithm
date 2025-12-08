def solution(n, words):
    answer = [0, 0]
    word_set = set()
    who = 0
    rotate = 1
    l = len(words)
    for i in range(l) :
        tmp = words[i]
        who += 1
        if who > n :
            rotate += 1
            who = 1
        # 끝말잇기가 맞는지 확인
        if i != 0 and tmp[0] != words[i-1][-1] :
            return [who, rotate]
        # 이미 한 적이 있는지 확인
        if tmp in word_set :
            return [who, rotate]
        else :
            word_set.add(tmp)

    return answer