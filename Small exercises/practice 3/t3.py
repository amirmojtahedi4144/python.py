n = int(input())
m  = 0
while n > 0:
    yekan = n % 10
    m = m * 10 + yekan
    n //= 10
    print(m)