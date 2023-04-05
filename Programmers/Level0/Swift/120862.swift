//
//  120862.swift
//
//  Created by 김유빈 on 2023/04/05.
//  최댓값 만들기 (2)

import Foundation

func solution(_ numbers:[Int]) -> Int {
    var nums: [Int] = numbers.sorted()
    var cnt: Int = numbers.count
    return max(nums[0] * nums[1], nums[cnt - 1] * nums[cnt - 2])
}

print(solution1([1, 2, -3, 4, -5])) // 15
print(solution2([0, -31, 24, 10, 1, 9])) // 240
print(solution2([10, 20, 30, 5, 5, 20, 5])) // 600
