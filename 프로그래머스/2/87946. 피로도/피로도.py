def ref(a, p, d, v, s) :
    for n in range(len(d)) :
        if not v[n] :
            v[n] = True
            if p >= d[n][0] :
                ref(a+1, p-d[n][1], d, v, s)
            v[n] = False
    else :
        s.append(a)
    
        

def solution(k, dungeons):
    ans = 0
    stack = []
    visit = [False for i in dungeons]
    ref(ans, k, dungeons, visit, stack)
    
    return max(stack)