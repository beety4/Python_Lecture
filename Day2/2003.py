arr = list(map(int, input().split()))
divisor = int(input())

answer = []
for num in arr:
    if num % divisor == 0:
        answer.append(num)

if len(answer) == 0:
    answer.append(-1)

print(sorted(answer))
