def solution(storey):
    ans = 0
    share = -1
    tmp = -1
    while storey != 0 :
        tmp = storey % 10
        share = storey // 10
        if tmp < 5 :
            ans += tmp
            storey = share
        if tmp > 5 :
            ans += (10-tmp)
            storey = share+1
        if tmp == 5 :
            if share % 10 >= 5 :
                ans += (10-tmp)
                storey = share+1
            else :
                ans += tmp
                storey = share
                
    return ans