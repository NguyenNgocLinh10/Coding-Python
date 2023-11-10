import base64


def greatestCommonPrimeDivisor(a,b):
    prime=[]
    both=[]
    for i in range(1, b+1):
        if a%i==0 and b%i==0:
            both.append(i)
    for i in both:
        c=0
        for x in range(1, int(i)+1):
            if int(i)%x == 0:
                c += 1
        if c == 2:
            prime.append(i)
            c = 0
        else:
            c = 0
            continue
    if len(prime)!= 0:
        ans=prime[-1]
    else:
        ans = -1
    return ans

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

print(greatestCommonPrimeDivisor(a,b))