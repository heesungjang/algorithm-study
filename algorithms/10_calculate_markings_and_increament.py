import sys

sys.stdin = open("input.txt", "rt")

n = int(input())

marking_sheet = list(map(int, input().split()))

total = 0
cnt = 0

for i in range(len(marking_sheet)):
    if marking_sheet[i] == 1:
        cnt += 1
        total += cnt
    else:
        cnt = 0

print(total)