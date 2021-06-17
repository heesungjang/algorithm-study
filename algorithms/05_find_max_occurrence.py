
import sys

sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

occurrence_list = [0] * (n+m)
max_occurrence = 0


for i in range(1, n+1):
    for j in range(1, m+1):
        occurrence_list[i+j-1] += 1

for i in range(n+m):
    if occurrence_list[i] > max_occurrence:
        max_occurrence = occurrence_list[i]

for i in range(n+m):
    if occurrence_list[i] == max_occurrence:
        print(i+1, end=' ')

