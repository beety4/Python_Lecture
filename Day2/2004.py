original = input()

answer = ""
other = ""
word = ["zero", "one", "two", "three", "four",
           "five", "six", "seven", "eight", "nine"]
for o in original:
    if o.isdigit():
        answer += o
        continue

    other += o
    if other in word:
        answer += str(word.index(other))
        other = ""

print(int(answer))