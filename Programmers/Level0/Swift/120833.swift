//
//  120833.swift
//
//  Created by 김유빈 on 2023/03/06.
//  배열 자르기

import Foundation

// 처음에 작성한 풀이
func solution(_ numbers:[Int], _ num1:Int, _ num2:Int) -> [Int] {
    return Array(numbers[num1...num2])
}

// 참고 풀이
func solution2(_ numbers:[Int], _ num1:Int, _ num2:Int) -> [Int] {
    return (num1...num2).map{numbers[$0]}
}

print(solution([1, 2, 3, 4, 5], 1, 3)) // [2, 3, 4]
print(solution([1, 3, 5], 1, 2)) // [3, 5]

print(solution2([1, 2, 3, 4, 5], 1, 3)) // [2, 3, 4]
print(solution2([1, 3, 5], 1, 2)) // [3, 5]
