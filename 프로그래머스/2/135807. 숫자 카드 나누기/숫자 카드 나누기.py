def solution(arrayA, arrayB):
    result_A, result_B = 0, 0
    def gcd(a, b) :
        if a < b :
            a, b = b, a
        while b > 0 :
            a, b = b, a % b
        return a
    for i in range(len(arrayA)) :
        if i == 0 :
            result_A = arrayA[i]
        else :
            result_A = gcd(result_A, arrayA[i])
    result_A = result_A if all(x % result_A != 0 for x in arrayB) else 0
    for i in range(len(arrayB)) :
        if i == 0 :
            result_B = arrayB[i]
        else :
            result_B = gcd(result_B, arrayB[i])
    result_B = result_B if all(x % result_B != 0 for x in arrayA) else 0
    return max(result_A, result_B)