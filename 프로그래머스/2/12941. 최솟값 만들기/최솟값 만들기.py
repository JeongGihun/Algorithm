def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)

    for i in range(len(A)) :
        answer += (A[i]*B[i])
    
    return answer

# [1, 2, 3, 4, 5] / [10, 8, 6, 4, 2]