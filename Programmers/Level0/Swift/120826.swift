//
//  120826.swift
//  
//
//  Created by 김유빈 on 2023/03/07.
//  특정 문자 제거하기

import Foundation

// 처음에 작성한 풀이
func solution(_ my_string: String, _ letter: String) -> String {
    return my_string.components(separatedBy: letter).joined()
}

// 참고 풀이
func solution2(_ my_string: String, _ letter: String) -> String {
    return my_string.filter{ String($0) != letter }
}

print(solution("abcdef", "f")) // "abcde"
print(solution("BCBDbe", "B")) // "Cdbe"

print(solution2("abcdef", "f")) // "abcde"
print(solution2("BCBDbe", "B")) // "Cdbe"
