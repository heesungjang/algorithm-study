import sys

sys.stdin = open("input.txt", "rt")

n = int(input())

numbers = list(map(int, input().split()))
max_total = 0
result = None


def digit_sum(x):
    total = 0
    for s in str(x):
        total += int(s)
    return total


for i in numbers:
    if digit_sum(i) > max_total:
        max_total = digit_sum(i)
        result = i

print(result)
