n = int(input())

money = [10000, 5000, 1000, 500, 100, 50, 10]
result = []

for m in money:
    if (n // m) > 0:
        result.append(f"{m} : {n // m}")
        n %= m

for r in result:
    print(r)
