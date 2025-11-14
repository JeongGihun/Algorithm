def solution(array, commands):
    answer = []
    num = len(commands)
    for i in range(num) :
        l = array[commands[i][0]-1:commands[i][1]]
        l.sort()
        answer.append(l[commands[i][2]-1])
    
    return answer