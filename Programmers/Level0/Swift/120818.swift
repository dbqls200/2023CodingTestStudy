//
//  120818.swift
//  
//
//  Created by 김유빈 on 2023/03/07.
//  옷가게 할인 받기

import Foundation

func solution(_ price:Int) -> Int {
    switch(price) {
        case(100000..<300000): return Int(Double(price) * 0.95)
        case(300000..<500000): return Int(Double(price) * 0.9)
        case(500000...): return Int(Double(price) * 0.8)
        default: return Int(Double(price))
    }
}

print(solution(150,000)) // 142,500
print(solution(580,000)) // 464,000
