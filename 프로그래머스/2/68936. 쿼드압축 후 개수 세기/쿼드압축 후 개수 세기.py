def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    def ref(x, y, l) :
        check = arr[y][x]
        if all(check == arr[j][i] 
               for j in range(y, y+l)
               for i in range(x, x+l)) :
            answer[check] += 1
            return
        
        ref(x, y, l//2)
        ref(x+l//2, y, l//2)
        ref(x, y+l//2, l//2)
        ref(x+l//2, y+l//2, l//2)
        
    ref(0, 0, n)   
    
    return answer