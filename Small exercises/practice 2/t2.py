time = int(input("enter the time:"))
hour = time // 3600
min = time // 60
sec = time % 60
print(f"{hour:02d}:{min:02d}:{sec:02d}")