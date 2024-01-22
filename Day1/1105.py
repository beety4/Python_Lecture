repeat = int(input())

data = {'국어': 0, '수학': 0, '영어': 0}
for i in range(repeat):
    val = input().split()

    if int(val[1]) >= 70:
        average = data.get(val[0])
        if average == 0:
            data[val[0]] = int(val[1])
        else:
            data[val[0]] = (average + int(val[1])) / 2

print(data)
