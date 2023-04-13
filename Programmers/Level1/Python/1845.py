# 1845 폰켓몬

def solution(nums):
    return len(nums) // 2 if len(nums) // 2 <= len(set(nums)) else len(set(nums))

def solution2(nums):
    return min(len(nums) // 2, len(set(nums)))

def test_sample():
    assert solution([3,1,2,3]) == 2
    assert solution([3,3,3,2,2,4]) == 3
    assert solution([3,3,3,2,2,2]) == 2

    assert solution2([3,1,2,3]) == 2
    assert solution2([3,3,3,2,2,4]) == 3
    assert solution2([3,3,3,2,2,2]) == 2
