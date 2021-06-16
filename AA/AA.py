# 1. N명의 학생의 평균을 구하고
# 2. N명의 학생 중 평균에 가장 가까운 학생은 몇명인지 출력
# 3. 평균에 가까운 사람이 여렃일 경우 빠른 학생의 번호 출력

import sys

sys.stdin = open("input.txt", "rt")

n = int(input())

min_num = 2147000000

grades = list(map(int, input().split()))
avg = round(sum(grades) / n)

for i, grade in enumerate(grades):
    tmp = abs(grade - avg)
    if tmp < min_num:
        min_num = tmp
        score = grade
        res = i + 1
    elif tmp == min_num:
        if grade > score:
            score = grade
            res = i + 1

print(avg, res)