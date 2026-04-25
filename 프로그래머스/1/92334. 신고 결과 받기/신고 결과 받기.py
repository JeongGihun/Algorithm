def solution(id_list, report, k):
    sign = {x:[] for x in id_list}
    check = {x:0 for x in id_list}
    for declaration in report :
        f, t = declaration.split()
        if t not in sign[f] :
            sign[f].append(t)
            check[t] += 1
    l = [i for i in check if check[i] >= k]
    ans = []
    for id in id_list :
        cnt = 0
        for tmp in sign[id] :
            if tmp in l :
                cnt += 1
        ans.append(cnt)
    return ans