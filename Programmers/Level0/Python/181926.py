# 181926 수 조작하기 1

def solution(n, control):
    controls = {
        'w': 1,
        's': -1,
        'd': 10,
        'a': -10
        }

    for c in control:
        n += controls[c]

    return n

def test_sample():
    assert solution(0, "wsdawsdassw") == -1

test_sample()
