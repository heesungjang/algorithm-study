import sys

sys.stdin = open("input.txt", "rt")


n = int(input())

filter_arr = [0] * (n+1)

count = 0

for i in range(2, n+1):
    if filter_arr[i] == 0:
        count += 1
        for j in range(i, n+1, i):
            filter_arr[j] = 1

print(count)


