altura=int(input())
if altura >=2 and altura <=9:
    for i in range(1,altura):
        for j in range(1,altura+1):
            print(j*altura)
else:
    print("error")