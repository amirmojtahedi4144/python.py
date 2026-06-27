def sum_digits(num):
    s = 0
    while True:
        s += num % 10
        num //= 10
    return s
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_nth_prime_after_n(n):
    b = sum_digits(n)
    count = 0
    num = n + 1
    while count < b:
        if is_prime(num):
            count += 1
        if count == b:
            c = num
            break
        num += 1
    return c
n = int(input("یک عدد صحیح وارد کنید: "))
c = find_nth_prime_after_n(n)
print(f"مجموع ارقام {n} برابر است با {sum_digits(n)}")
print(f"{sum_digits(n)}مین عدد اول پس از {n} برابر است با {c}")