# 스택 예제

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력



# 큐 예제

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기 
print(queue) # 나중에 들어온 원소부터 출력 


# 재귀 함수 예제

def recursive_function():
    print("재귀 함수를 호출합니다.")
    recursive_function()

recursive_function()
