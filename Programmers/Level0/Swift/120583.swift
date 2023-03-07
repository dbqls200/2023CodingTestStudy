//
//  120583.swift
//  
//
//  Created by 김유빈 on 2023/03/07.
//  중복된 숫자 개수

import Foundation

func solution(_ array:[Int], _ n:Int) -> Int {
    return array.filter{ $0 == n }.count
}

print(solution([1, 1, 2, 3, 4, 5], 1)) // 2
print(solution([0, 2, 3, 4], 1)) // 0
