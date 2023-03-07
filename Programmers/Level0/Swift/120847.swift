//
//  120847.swift
//  
//
//  Created by 김유빈 on 2023/03/07.
//  최댓값 만들기(1)

import Foundation

func solution(_ numbers:[Int]) -> Int {
    var numbers: [Int] = numbers.sorted(by: >)
    return numbers[0] * numbers[1]
}

print(solution([1, 2, 3, 4, 5])) // 20
print(solution([0, 31, 24, 10, 1, 9])) // 744
