a = input()
b = input()
c = input()

if (a + b > c) or (a + c > b) or (b + c > a):
    if a == b == c:
        print("Equilateral triangle")
    elif a == b and a == c and b == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")