import string
import math
def solution(str1, str2):
    answer = 0
    l1 = list(str1)
    l2 = list(str2)
    sen = {}
    max_num = 0
    min_num = 0
    
    # 대문자는 소문자로 변환
    l1 = list(map(lambda x : chr(ord(x)+32) if 65<=ord(x)<=90 else x, l1))
    l2 = list(map(lambda x : chr(ord(x)+32) if 65<=ord(x)<=90 else x, l2))
    
    # 특수문자를 제거하고, 붙어있는 영문자 2개를 딕셔너리에 삽입
    # 딕셔너리 구조는 {문자 : l1개수, l2개수}. 전부 97~122겠지
    for i in range(len(l1)-1) :
        tmp = l1[i:i+2]
        for j in range(2) :
            if ord(tmp[j]) < 97 or ord(tmp[j]) > 122 :
                print(tmp)
                break
        else :
            tmp = ''.join(tmp)
            if tmp not in sen :
                sen[tmp] = [0, 0]
            sen[tmp][0] += 1
        
    for i in range(len(l2)-1) :
        tmp = l2[i:i+2]
        for j in range(2) :
            if ord(tmp[j]) < 97 or ord(tmp[j]) > 122 :
                break
        else :
            tmp = ''.join(tmp)
            if tmp not in sen :
                sen[tmp] = [0, 0]
            sen[tmp][1] += 1
    
    # 공통 : min_num / 전체 : max_num
    for k,v in sen.items() :
        max_num += max(v[0], v[1])
        min_num += min(v[0], v[1])
    
    # max_num이 0인 경우 div가 불가
    if max_num == 0 :
        result = 65536
        return result
    else :
        result = math.floor((min_num / max_num) * 65536)
        return result