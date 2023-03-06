//
//  120830.swift
//
//  Created by 김유빈 on 2023/03/06.
//  양꼬치

import Foundation

func solution(_ n: Int) -> Int {
    return n * 12000 + (k - (n / 10)) * 2000
}

print(solution(10, 3)) // 124,000
print(solution(64, 6)) // 768,000
