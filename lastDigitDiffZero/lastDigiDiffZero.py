def lastDigitDiffZero(n):
    a = 1
    ans = []
    for i in range(1, n + 1):
        a *= i
        b = str(a)
    for j in b:
        if j != '0':
            ans.append(j)
    return int(ans[-1])

n = int(input("Nhập n: "))
print(lastDigitDiffZero(n))