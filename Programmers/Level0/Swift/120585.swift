//
//  120585.swift
//  
//
//  Created by 김유빈 on 2023/03/07.
//  머쓱이보다 키 큰 사람

import Foundation

func solution(_ array:[Int], _ height:Int) -> Int {
    return array.filter{ $0 > height }.count
}

print(solution([149, 180, 192, 170], 167)) // 3
print(solution([180, 120, 140], 190)) // 0
