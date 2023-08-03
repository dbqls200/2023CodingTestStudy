# 181906 접두사인지 확인하기

# for문 돌면서 같은지 확인하기
def solution1(my_string, is_prefix):

    if len(is_prefix) <= len(my_string):
        for i in range(len(is_prefix)):
            if is_prefix[i] != my_string[i]:
                return 0

        return 1
    return 0



# 내장함수 사용하기
def solution2(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))



def test_sample():
    assert solution1("banana", "ban") == 1
    assert solution1("banana", "bananan") == 0
    assert solution1("banana", "abcd") == 0

    assert solution2("banana", "ban") == 1
    assert solution2("banana", "bananan") == 0
    assert solution2("banana", "abcd") == 0


test_sample()
