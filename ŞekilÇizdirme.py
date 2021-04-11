for i in range(0,11):
    if i==0 or i==10:
        for j in range(0,11):
            print("-",end="")
    if i==1 or i==9:
        for j in range(0,11):
            if j!=5:
                print("-",end="")
            else:
                print("+",end="")
    if i==2 or i==8:
        for j in range(0,11):
            if j<3 or j>7:
                print("-",end="")
            else:
                print("+",end="")
    if i==3 or i==7:
        for j in range(0,11):
            if j<2 or j>8:
                print("-",end="")
            else:
                print("+",end="")
    if i==4 or i==6:
        for j in range(0,11):
            if j<2 or j>8:
                print("-",end="")
            else:
                print("+",end="")
    if i==5:
        for j in range(0,11):
            if j==0 or j==10:
                print("-",end="")
            else:
                print("+",end="")
    print("")