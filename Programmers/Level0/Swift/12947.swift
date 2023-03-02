//
//  12947.swift
//
//  Created by 김유빈 on 2023/03/02.
//  하샤드 수

import Foundation

func solution1(_ x:Int) -> Bool {
    var sum = 0
    
    for i in String(x) {
        sum += Int(String(i))!
    }
    
    return x % sum == 0
}

// 고차함수를 이용한 답안
// 참고용으로 추가해둠
func solution2(_ x:Int) -> Bool {
    var sum = String(x)
        .map { Int(String($0))! }
        .reduce(0, +)

    return x % sum == 0
}

print(solution1(10)) // true
print(solution2(12)) // true
