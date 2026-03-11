def solution(numbers):
    numbers.sort()
    ans = numbers.pop() * numbers.pop()
    return ans