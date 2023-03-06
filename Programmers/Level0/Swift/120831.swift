//
//  120831.swift
//
//  Created by 김유빈 on 2023/03/06.
//  짝수의 합

import Foundation

// 처음에 작성한 풀이
func solution(_ n: Int) -> Int {
    var result: Int = 0
    for i in 1...n {
        if i % 2 == 0 { result += i}
    }
    return result
}

// 참고 풀이
func solution2(_ n: Int) -> Int {
    return (0...n).filter { $0 % 2 == 0 }.reduce(0, +)
}

print(solution(10)) // 30
print(solution(4)) // 6

print(solution2(10)) // 30
print(solution2(4)) // 6
