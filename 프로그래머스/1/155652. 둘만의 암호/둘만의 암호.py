import string
def solution(s, skip, index):
    answer = ''
    change_list = list(string.ascii_lowercase)
    s = list(s)
    change_list = [x for x in change_list if x not in list(skip)]
    
    for i in range(len(s)) :
        tmp = change_list.index(s[i])+index
        s[i] = change_list[tmp%len(change_list)]
        
    return ''.join(s)