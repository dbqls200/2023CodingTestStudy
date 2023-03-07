//
//  120813.swift
//  
//
//  Created by 김유빈 on 2023/03/07.
//  짝수는 싫어요

import Foundation

// 처음에 작성한 풀이
func solution(_ n:Int) -> [Int] {
    var result: [Int] = []
    for i in (1...n) {
     if i % 2 != 0 {
        result.append(i)
     }
    }
    return result
}

// 참고 풀이
func solution2(_ n: Int) -> [Int] {
    return (0...n).filter { $0 % 2 == 1 }
}

print(solution(10)) // [1, 3, 5, 7, 9]
print(solution(15)) // [1, 3, 5, 7, 9, 11, 13, 15]
