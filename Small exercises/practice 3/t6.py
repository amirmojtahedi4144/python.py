n = int(input("یک عدد وارد کنید: "))

total = 0
count = 0
i = 1
while i <= n:
    total = total + i
    count = count + 1
    i = i + 1
print(f"مجموع ۱ تا {n} = {total}")
print(f"تعداد کامپوننت‌های تولید شده: {count}")
print(f"تعداد کل بار تولید و چاپ: {count}")