//
//  120841.swift
//  
//
//  Created by 김유빈 on 2023/03/07.
//  점의 위치 구하기

import Foundation

func solution(_ dot:[Int]) -> Int {
    return dot[0] > 0 && dot[1] > 0 ? 1 : dot[1] > 0 ? 2 : dot[0] > 0 ? 4 : 3
}

print(solution([2, 4])) // 1
print(solution([-7, 9])) // 2
