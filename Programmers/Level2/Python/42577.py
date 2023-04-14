# 42577 전화번호 목록

def solution(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True

def solution2(phone_book):
    hashDict = {}

    for number in phone_book:
        hashDict[number] = 1

    for number in phone_book:
        temp = ''

        for num in number:
            temp += num

            if temp in hashDict and temp != number:
                return False

    return True


def test_sample():
    assert solution(["119", "97674223", "1195524421"]) == False
    assert solution(["123","456","789"]) == True
    assert solution(["12","123","1235","567","88"]) == False

    assert solution2(["119", "97674223", "1195524421"]) == False
    assert solution2(["123","456","789"]) == True
    assert solution2(["12","123","1235","567","88"]) == False


test_sample()
