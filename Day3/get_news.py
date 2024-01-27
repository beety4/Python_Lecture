with open("news_rank.txt", 'r', encoding="UTF-8") as f:
    data = {}
    while True:
        line = f.readline().strip()
        if line == "":
            break

        data[line] = f.readline().strip().split("|")


for key, value in data.items():
    print(key)
    print(value)
