def solution(players, callings):
    rank = dict()
    for i, k in enumerate(players) :
        rank[k] = i+1
    
    for call in callings :
        n = rank[call] - 1
        players[n], players[n-1] = players[n-1], players[n]
        
        rank[players[n]] = n+1
        rank[players[n-1]] = n
        
    return players