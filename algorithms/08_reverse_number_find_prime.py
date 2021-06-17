import sys

sys.stdin = open("input.txt", "rt")

n = int(input())

numbers = list(map(int, input().split()))


def reverse(x):
    res = 0
    while x > 0:
        tmp = x % 10
        res = (res * 10) + tmp
        x = x // 10
    return res


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i ==0:
            return False
    else:
        return True


for num in numbers:
    tmp = reverse(num)
    if is_prime(tmp):
        print(tmp, end=" ")
