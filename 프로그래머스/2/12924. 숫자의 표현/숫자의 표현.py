def solution(n):
    ans = 0
    s, e = 0, 0
    num = [i for i in range(n+1)]
    sum_ = 0
    while e < n :
        if num == s :
            break
        if sum_ == n :
            ans += 1
            e += 1
            sum_ += num[e]
        elif sum_ > n :
            s += 1
            sum_ -= num[s]
        elif sum_ < n :
            e += 1
            sum_ += num[e]
    return ans+1