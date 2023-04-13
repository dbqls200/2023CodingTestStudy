# 17681 [1차] 비밀지도

def solution(n, arr1, arr2):
    binary_map = []

    # 지도 1, 2 비교
    for i in range(len(arr1)):
        binary_map.append(bin(arr1[i] | arr2[i])[2:].zfill(n))

        # 1 -> "#", 0 -> " "으로 변환
        for i in range(len(binary_map)):
            binary_map[i] = binary_map[i].replace("1", "#").replace("0", " ")

    print(binary_map)
    return binary_map

def test_sample():
    assert solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]) ==  ['#####','# # #', '### #', '# ##', '#####'], "값 틀림"
    assert solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]) == ["######", "### #", "## ##", " #### ", " #####", "### # "], "값 틀림"

test_sample()
