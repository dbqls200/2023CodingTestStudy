# 17680 [1차] 캐시

def solution(cacheSize, cities):
    answer += 0
    cache = []

    for city in cities:
        if not city.lower() in cache:
            cache.append(city.lower())
            answer += 5
            if len(cache) > cacheSize:
                cache.pop(0)
        else:
            answer += 1
            cache.pop(cache.index(city.lower()))
            cache.append(city.lower())

    return answer
