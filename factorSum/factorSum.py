def factorSum(n):
    m = n
    s = 0
    k = 2
    while m > 1:
        while m % k == 0:
            s += k
            m /= k
        k += 1
    if n != s:
        return(factorSum(s))
    else:
        return(n)
n = int(input("Nhập n"))
print(factorSum(n))