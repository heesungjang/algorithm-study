import sys

sys.stdin = open("input.txt", "rt")

test_cases = int(input())

for i in range(test_cases):
    n, s, e, k = map(int, input().split())
    test_values = list(map(int, input().split()))

    target_values = test_values[s-1:e]
    target_values.sort()

    result = target_values[k-1]

    print(f"#{i+1} {result}")
