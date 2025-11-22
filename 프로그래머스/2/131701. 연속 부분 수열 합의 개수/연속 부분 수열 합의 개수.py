def solution(elements):
    answer = 0
    num = len(elements)
    s = set()
    for i in range(num) :
        # i는 이번에 몇 개 넣는지
        check = sum(elements[:i+1])
        s.add(check) # 이거까진 맞음
        for j in range(num) :
            check += elements[i+j+1 if i+j+1 < num else i+j+1-num]
            check -= elements[j]
            #print(j, i+j+1 if i+j+1 < num else i+j+1-num)
            s.add(check)
    return len(s)