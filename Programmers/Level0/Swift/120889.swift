//
//  120889.swift
//  
//
//  Created by 김유빈 on 2023/03/07.
//  삼각형의 완성조건 (1)

import Foundation

// 처음에 작성한 풀이
func solution(_ sides:[Int]) -> Int {
    return sides.max() ?? 0 < (sides.reduce(0, +) - (sides.max() ?? 0)) ? 1 : 2
}

// 참고 풀이
func solution2(_ sides: [Int]) -> Int {
    var sortedSides: [Int] = sides.sorted()
    return sortedSides[0] + sortedSides[1] > sortedSides[2] ? 1 : 2
}

print(solution([1, 2, 3])) // 2
print(solution([3, 6, 2])) // 2
print(solution([199, 72, 222])) // 1

print(solution2([1, 2, 3])) // 2
print(solution2([3, 6, 2])) // 2
print(solution2([199, 72, 222])) // 1
