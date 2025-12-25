from collections import deque
def solution(cacheSize, cities):
    ans = 0
    cache = []
    cacheSize = min(cacheSize, 30)
    # 소문자화
    for i in range(len(cities)) :
        cities[i] = cities[i].lower()

    for i in cities :
        for j in range(len(cache)) :
            if i == cache[j] :
                ans += 1
                del cache[j]
                cache.append(i)
                break
        else :
            if cacheSize != 0 :
                if len(cache) == cacheSize :
                    del cache[0]
                cache.append(i)
            ans += 5

    return ans