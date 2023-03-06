//
//  120816.swift
//
//  Created by 김유빈 on 2023/03/06.
//  피자 나눠 먹기 (3)

import Foundation

func solution(_ slice:Int, _ n:Int) -> Int {
    return ((n - 1) / slice) + 1
}

print(solution(7, 10)) // 2
print(solution(4, 12)) // 3
