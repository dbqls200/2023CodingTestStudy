# 42576 완주하지 못한 선수

def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for p in participant:
        hashDict[hash(p)] = p
        sumHash += hash(p)

    for c in completion:
        sumHash -= hash(c)

    return hashDict[sumHash]

def test_sample():
    assert solution(["leo", "kiki", "eden"], 	["eden", "kiki"]) == "leo"
    assert solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]) == "vinko"
    assert solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) == "mislav"


test_sample()
