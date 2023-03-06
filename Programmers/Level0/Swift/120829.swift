//
//  120829.swift
//
//  Created by 김유빈 on 2023/03/06.
//  각도기

import Foundation

// 처음에 작성한 풀이
func solution(_ angle: Int) -> Int {
    if angle > 0 && angle < 90 { return 1 }
    else if angle == 90 { return 2 }
    else if angle > 90 && angle < 180 { return 3 }
    else { return 4 }
}

// 참고 풀이
func solution2(_ angle: Int) -> Int {
    return angle < 90 ? 1 : angle == 90 ? 2 : angle < 180 ? 3 : 4
}

print(solution(70)) // 1
print(solution(91)) // 3
print(solution(180)) // 4

print(solution2(70)) // 1
print(solution2(91)) // 3
print(solution2(180)) // 4
