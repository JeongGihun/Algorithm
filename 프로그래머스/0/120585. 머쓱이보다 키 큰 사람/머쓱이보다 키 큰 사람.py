def solution(array, height):
    answer = 0
    for people in array :
        if people > height :
            answer += 1
    return answer