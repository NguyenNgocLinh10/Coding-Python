a = int(input)
Tong = 0
for x in range(1, a):
    if a % x == 0:
        Tong += x

print(Tong)