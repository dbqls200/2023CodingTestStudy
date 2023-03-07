//
//  120825.swift
//  
//
//  Created by 김유빈 on 2023/03/07.
//  문자 반복 출력하기

import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    return my_string.map{ String(repeating: $0, count: n) }.joined()
}

print(solution("hello", 3)) // "hhheeellllllooo"
