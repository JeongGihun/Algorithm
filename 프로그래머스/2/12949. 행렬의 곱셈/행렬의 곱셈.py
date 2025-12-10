def solution(arr1, arr2):
    # arr1_y * arr2_x
    arr1_x, arr1_y, arr2_x, arr2_y = len(arr1[0]), len(arr1), len(arr2[0]), len(arr2)
    answer = [[0 for j in range(arr2_x)] for i in range(arr1_y)] 
    
    for i in range(arr1_y) :
        for j in range(arr2_x) :
            tmp = 0
            for k in range(arr1_x) :
                tmp += arr1[i][k] * arr2[k][j]
            answer[i][j] = tmp
    return answer