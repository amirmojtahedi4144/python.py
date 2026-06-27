x , z = map(int,input().split())
yekan1 = x % 10
y = (x - yekan1) // 10
dahgan1 = y % 10
sadgan1 = (y - dahgan1) // 10
x2 = yekan1 * 100 + dahgan1 * 10 + sadgan1
yekan2 = x % 10
m = (z - yekan2) // 10
dahgan2 = m % 10
sadgan2 = ( m - dahgan2) // 10
z2 = yekan2 * 100 + dahgan2 * 10 + sadgan2
print(x2 , z2)
if x2 > z2:
    print(f"{x} > {z}")
else:
    print(f"{x} < {z}")