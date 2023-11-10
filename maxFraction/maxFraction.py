def maxFraction(numerators, denominators):
    a = []
    for i in range(len(denominators)):
        a.append(int(numerators[i]) / int(denominators[i]))
    return a.index(max(a))

numerators = []
n =int(input("Nhập vào sô phần tử của mảng tử: "))
for i in range(n):
   numerators.append(input("Phần tử của mảng: " ))
   
denominators = []
n =int(input("Nhập vào sô phần tử của mảng mẫu: "))
for i in range(n):
   denominators.append(input("Phần tử của mảng: "))
   
print(maxFraction(numerators, denominators))