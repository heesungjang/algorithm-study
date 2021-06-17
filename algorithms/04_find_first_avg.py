import sys

sys.stdin = open("input.txt", "rt")

n = int(input())

min_num = 2147000000

grades = list(map(int, input().split()))
avg = round(sum(grades) / n)
current_score = 0
for i, grade in enumerate(grades):
    tmp = abs(grade - avg)
    if tmp < min_num:
        min_num = tmp
        current_score = grade
        res = i + 1
    elif tmp == min_num:
        if grade > current_score:
            score = grade
            res = i + 1

print(avg, res)