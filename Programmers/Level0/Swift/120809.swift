//
//  120809.swift
//
//  Created by 김유빈 on 2023/03/06.
//  배열 두 배 만들기

import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    return numbers.map { $0 * 2 }
}

print(solution([1, 2, 3, 4, 5])) // [2, 4, 6, 8, 10]
print(solution([1, 2, 100, -99, 1, 2, 3])) // [2, 4, 200, -198, 2, 4, 6]
