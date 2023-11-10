def digitsProduct(product):
    if product == 0:
        return 10
    if product == 1:
        return 1
    
    factors = []
    for i in range(9, 1, -1):
        while product % i == 0:
            product //= i
            factors.append(i)

    if product != 1:
        return -1
    return int("".join(map(str, factors[::-1])))

product = int(input("Nhập số: "))
print(digitsProduct(product))