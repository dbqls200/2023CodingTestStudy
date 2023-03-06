//
//  120806.swift
//
//  Created by 김유빈 on 2023/03/06.
//  두 수의 나눗셈

import Foundation

// 처음에 작성한 풀이
func solution(_ num1: Int, _ num2: Int) -> Int {
    return Int((Double(num1) / Double(num2)) * 1000)
}

// 참고한 풀이
func solutio2(_ num1: Int, _ num2: Int) -> Int {
    return num1 * 1000 / num2
}


print(solution(3, 2)) // 1500
print(solution(7, 3)) // 2333
print(solution(1, 16)) // 62

print(solution2(3, 2)) // 1500
print(solution2(7, 3)) // 2333
print(solution2(1, 16)) // 62
