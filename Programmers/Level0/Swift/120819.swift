//
//  120819.swift
//  
//
//  Created by 김유빈 on 2023/03/07.
//  아이스 아메리카노

import Foundation

func solution(_ money:Int) -> [Int] {
    return [money / 5500, money % 5500]
}

print(solution(5500)) // [1, 0]
print(solution(15000)) // [2, 4000]
