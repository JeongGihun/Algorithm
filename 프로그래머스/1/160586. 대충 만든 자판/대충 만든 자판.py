def solution(keymap, targets):
    ans = []
    check = dict()
    
    for i in range(len(keymap)) :
        for j in range(len(keymap[i])) :
            if keymap[i][j] in check :
                check[keymap[i][j]] = min(check[keymap[i][j]], j+1)
            else :
                check[keymap[i][j]] = j+1
    
    for target in targets :
        num = 0
        for tmp in target :
            if tmp not in check :
                ans.append(-1)
                break
            num += check[tmp]
        else :
            ans.append(num)
    return ans