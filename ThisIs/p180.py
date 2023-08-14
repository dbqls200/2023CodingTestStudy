# p.180 성적이 낮은 순서로 학생 출력하기


n = int(input())

array = []
for _ in range(n):
    data = input().split()
    array.append((data[0], data[1]))

array = sorted(array, key = lambda x: data[1])

for i in range(len(array)):
    print(array[i][0], end=' ')
