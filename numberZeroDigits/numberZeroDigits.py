def numberZeroDigits(n):
    count = 0
    k = 5
    while k <= n:
        count += n // k
        k *= 5
    return count

n = int(input("Nhập n: "))
print(numberZeroDigits(n))