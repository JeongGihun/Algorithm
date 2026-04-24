
    

def solution(mats, park):
    ans = -1
    x, y = len(park[0]), len(park)
    
    def ref(a, b, c) :
        flag = True
        for dx in range(c) :
            for dy in range(c) :
                if 0 <= b+dy < y and 0 <= a+dx < x :
                    if park[b+dy][a+dx] != "-1" :
                        flag = False
                else :
                    flag = False
        return flag
    
    for j in range(y) :
        for i in range(x) :
            if park[j][i] == "-1" :
                for k in mats :
                    if ref(i, j, k) :
                        ans = max(ans, k)
    
    return ans