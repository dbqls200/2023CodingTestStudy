//
//  120807.swift
//
//  Created by 김유빈 on 2023/03/06.
//  두 수의 차

import Foundation

func solution(_ num1:Int, _ num2:Int) -> Int {
    return num1 == num2 ? 1 : -1
}

print(solution(2, 3)) // -1
print(solution(11, 11)) // 1
print(solution(7, 99)) // -1
