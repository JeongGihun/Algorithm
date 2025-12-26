from collections import deque
dictionary = set()
dictionary_remake = set()
def rep(n, x, list_, check_list, number) :
    if n == x :
        return
    for i in range(len(list_)) :
        if check_list[i] == False :
            check_list[i] = True
            number += list_[i]
            dictionary.add(number)
            rep(n+1, x, list_, check_list, number)
            check_list[i] = False
            number = number[:-1]
        
def solution(numbers):
    number = ''
    l = list(numbers)
    check = [False for i in numbers]
    rep(0, len(l), l, check, number)
    sosu = []
    
    for i in dictionary :
        dictionary_remake.add(int(i))
    
    for i in dictionary_remake :
        i = int(i)
        if i < 2 :
            continue
        for j in range(2, i) :
            if i % j == 0 :
                break
        else :
            sosu.append(i)
    
    return len(sosu)