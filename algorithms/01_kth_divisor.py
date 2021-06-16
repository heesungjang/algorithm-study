import sys
sys.stdin = open("input.txt", "rt")
# Question 1.
n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
    if count == k:
        print(count)
        break
else:
    print(-1)


