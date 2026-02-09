import re

def solution(files):
    answer = []
    check = []
    for file in files :
        tmp = re.findall(r'[^0-9]+|\d+', file)
        check.append(tmp)
    check.sort(key=lambda x : (x[0].upper(), int(x[1])))
    
    for i in check :
        answer.append(''.join(i))
    
    return answer