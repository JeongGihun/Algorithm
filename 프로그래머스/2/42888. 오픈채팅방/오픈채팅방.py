def solution(record):
    ans = []
    final = []
    idpool = dict()
    for i in record :
        tmp = i.split()
        
        if tmp[0] == "Enter" :
            ans.append([tmp[1], "님이 들어왔습니다."])
            idpool[tmp[1]] = tmp[2]
        if tmp[0] == "Leave" :
            ans.append([tmp[1], "님이 나갔습니다."])
        if tmp[0] == "Change" :
            idpool[tmp[1]] = tmp[2]
            idpool[tmp[1]] = tmp[2]
    
    for tmp in ans :
        final.append(idpool[tmp[0]] + tmp[1])
    
    return final