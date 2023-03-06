//
//  120821.swift
//
//  Created by 김유빈 on 2023/03/06.
//  배열 뒤집기

import Foundation

// 처음에 작성한 풀이
func solution(_ n: Int) -> Int {
    return num_list.reversed()
}

print(solution([1, 2, 3, 4, 5])) // [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 1, 2])) // [2, 1, 1, 1, 1, 1]
print(solution([1, 0, 1, 1, 1, 3, 5])) // [5, 3, 1, 1, 1, 0, 1]
