def ref(a, b, c, p) :
    b += p
    if b > 12 :
        a += (b-1) // 12
        b = (b-1) % 12 +1
    c -= 1
    if c < 1 :
        c += 28
        b -= 1
        if b < 1 :
            b += 12
            a -= 1
    return [a, b, c]

def solution(today, terms, privacies):
    ans = []
    l = dict()
    today = today.split(".")
    t_y, t_m, t_d = int(today[0]), int(today[1]), int(today[2])
    # 개월 수 입력
    for i in terms :
        plan, month = i.split()
        l[plan] = month
        
    for i in range(len(privacies)) :
        day, plan = privacies[i].split()
        y, m, d = day.split(".")
        y = int(y)
        m = int(m)
        d = int(d)
        plan = int(l[plan])
        tmp = ref(y, m, d, plan)
        y, m, d = list(tmp)
        
        if t_y > y :
            ans.append(i+1)
            print(t_y, t_m, t_d, y, m, d)
            continue
        if t_y == y and t_m > m :
            ans.append(i+1)
            print(t_y, t_m, t_d, y, m, d)
            continue
        if t_y == y and t_m == m and t_d > d :
            ans.append(i+1)
            print(t_y, t_m, t_d, y, m, d)
            continue
        
    return ans