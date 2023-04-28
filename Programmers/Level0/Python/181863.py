# 181863 rny_string

def solution(rny_string):
    return ''.join(['rn' if rny == 'm' else rny for rny in rny_string])

def solution2(rny_string):
    return rny_string.replace('m', 'rn')

def test_sample():
    assert solution('masterpiece') == 'rnasterpiece'
    assert solution('programmers') == 'prograrnrners'
    assert solution('jerry') == 'jerry'

    assert solution2('masterpiece') == 'rnasterpiece'
    assert solution2('programmers') == 'prograrnrners'
    assert solution2('jerry') == 'jerry'

test_sample()
