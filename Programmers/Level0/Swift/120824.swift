//
//  120824.swift
//
//  Created by 김유빈 on 2023/03/06.
//  짝수 홀수 개수

import Foundation

// 처음에 작성한 풀이
func solution(_ num_list:[Int]) -> [Int] {
    var result:[Int] = []
    var evenCnt: Int = 0
    var oddCnt: Int = 0
    for num in num_list {
        if num % 2 == 0 {
            evenCnt += 1
        }
        else {oddCnt += 1}
    }
    result.append(evenCnt)
    result.append(oddCnt)
    return result
}

// 참고 풀이
func solution2(_ num_list:[Int]) -> [Int] {
    return [num_list.filter{ $0 % 2 == 0 }.count, num_list.filter{ $0 % 2 != 0 }.count]
}

print(solution([1, 2, 3, 4, 5])) // [2, 3]
print(solution([[1, 3, 5, 7])) // [0, 4]
                
print(solution2([1, 2, 3, 4, 5])) // [2, 3]
print(solution2([[1, 3, 5, 7])) // [0, 4]
