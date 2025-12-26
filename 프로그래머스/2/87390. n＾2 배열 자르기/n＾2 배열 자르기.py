def solution(n, left, right):
    ans = []
    for i in range(left, right+1) :
        tmp_div = i // n + 1
        tmp_mod = i % n + 1
        #print(tmp_div, tmp_mod)
        ans.append(max(tmp_div, tmp_mod))
    
    return ans