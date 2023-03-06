//
//  120817.swift
//
//  Created by 김유빈 on 2023/03/06.
//  배열의 평균값

import Foundation

// 처음에 작성한 풀이
func solution(_ numbers:[Int]) -> Double {
    var result: Double = 0.0
    for num in numbers {
        result += Double(num)
    }
    return result / Double(numbers.count)
}

// 참고 풀이
func solution2(_ numbers:[Int]) -> Double {
    return Double(numbers.reduce(0, +)) / Double(numbers.count)
}

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) // 5.5
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])) // 94.0

print(solution2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) // 5.5
print(solution2([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])) // 94.0
