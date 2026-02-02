def solution(dirs):
    answer = 0
    check = set()
    l = len(dirs)
    dirs = list(dirs)
    x, y = 0, 0
    wasd = {'U' : (0, 1), 'D' : (0, -1), 'L' : (-1, 0), 'R' : (1, 0)}
    
    for dir in dirs :
        before = (x, y)
        if -5 <= x + wasd[dir][0] <= 5 and -5 <= y + wasd[dir][1] <= 5 :
            x = x + wasd[dir][0] 
            y = y + wasd[dir][1]
        
        after = (x, y)
        
        if before == after :
            continue
        
        if (before, after) not in check and (after, before) not in check :
            answer += 1
            
            check.add((before, after))
            check.add((after, before))
        print(before, after, answer)
        
    return answer