//
//  120811.swift
//  
//
//  Created by 김유빈 on 2023/03/07.
//  중앙값 구하기

import Foundation

func solution(_ array:[Int]) -> Int {
    return array.sorted()[array.count / 2]
}

print(solution([1, 2, 7, 10, 11])) // 7
print(solution([9, -1, 0])) // 0
