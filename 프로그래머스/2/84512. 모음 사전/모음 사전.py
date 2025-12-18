def mul(x) :
    if x == 0 :
        return 1
    return 5 * mul(x-1) + 1

def solution(word):
    ans = 0
    l = len(word)
    alpha = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    ans += l
    for i in range(l) :
        ans += (alpha[word[i]] - 0) * mul(4-i)
        #print(alpha[word[i]], mul(4-i))
    
    return ans