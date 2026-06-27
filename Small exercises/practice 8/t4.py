def data(temp_data:int):
    temp_data = int,input().split()
    print(temp_data)
    if temp_data > 20:
        print("max")
    elif temp_data < 15:
        print("min")
    elif temp_data // 0:
        print("this number is even")
    elif temp_data  :
        print("this number is odd")
    data(temp_data)
    print()