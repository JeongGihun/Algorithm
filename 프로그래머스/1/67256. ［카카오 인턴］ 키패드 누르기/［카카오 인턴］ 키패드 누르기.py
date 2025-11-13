def dis_chk(button):
    if button == 0 :
        return 3, 1
    elif button == '*' :
        return 3, 0
    elif button == '#' :
        return 3, 2
    else :
        return (button-1)//3, (button-1)%3

def solution(numbers, hand):
    answer = ''
    
    lh = '*'
    rh = '#'
    for i in numbers :
        tmp = i  # 이번에 무슨 숫자인지
        if tmp == 0 or tmp % 3 == 2 :
            l_x, l_y = dis_chk(lh)  # 왼손 위치
            r_x, r_y = dis_chk(rh)  # 오른손 위치
            n_x, n_y = dis_chk(tmp)
            
            l_dis = abs(n_x-l_x) + abs(n_y-l_y)  
            r_dis = abs(n_x-r_x) + abs(n_y-r_y)
            
            if l_dis > r_dis :
                answer += 'R'
                rh = tmp
            elif l_dis < r_dis :
                answer += 'L'
                lh = tmp
            else :
                if hand == "left" :
                    answer += 'L'
                    lh = tmp
                else :
                    answer += 'R'
                    rh = tmp
            
        elif tmp % 3 == 1 :
            answer += 'L'
            lh = tmp
        elif tmp % 3 == 0 :
            answer += 'R'
            rh = tmp
    
    return answer