//
//  120814.swift
//
//  Created by 김유빈 on 2023/03/06.
//  피자 나눠 먹기 (1)

import Foundation

func solution(_ n:Int) -> Int {
    return (n - 1) / 7 + 1
}

print(solution(7)) // 1
print(solution(1)) // 1
print(solution(15)) // 3
