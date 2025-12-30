def solution(wallet, bill):
    ans = 0
    if wallet[0] > wallet[1] :
        wallet[0], wallet[1] = wallet[1], wallet[0]
    
    while True :
        if bill[0] > bill[1] :
            bill[0], bill[1] = bill[1], bill[0]
        
        if wallet[0] >= bill[0] and wallet[1] >= bill[1] :
            break
        else :
            bill[1] //= 2
            ans += 1
        
    
    return ans