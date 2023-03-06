//
//  120854.swift
//
//  Created by 김유빈 on 2023/03/06.
//  배열 원소의 길이

import Foundation

// 처음에 작성한 풀이
func solution(_ strlist:[String]) -> [Int] {
    var result:[Int] = []
    for str in strlist {
        result.append(str.count)
    }
    return result
}

// 참고 풀이
func solution2(_ strlist:[String]) -> [Int] {
    return strlist.map{ $0.count }
}

print(solution(["We", "are", "the", "world!"])) // [2, 3, 3, 6]
print(solution(["I", "Love", "Programmers."])) // [1, 4, 12]

print(solution2(["We", "are", "the", "world!"])) // [2, 3, 3, 6]
print(solution2(["I", "Love", "Programmers."])) // [1, 4, 12]
