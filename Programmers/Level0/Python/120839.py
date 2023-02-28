# 120839 가위 바위 보

def solution(rsp):
    win = {'0': '5', '2': '0', '5': '2'}
    return ''.join([win[s] for s in rsp])
