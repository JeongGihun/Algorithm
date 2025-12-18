def solution(s):
    num = 0
    zero = 0
    length = 0
    
    while s != "1" :
        num += 1
        zero += s.count("0")
        length = len(s) - s.count("0")
        s = bin(length)[2:]
        
    return [num, zero]