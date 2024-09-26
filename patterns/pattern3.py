def pattten3(colums,row):
    for i in range(0,colums+1):
        for j in range(0,row+1):
            if i==0 or j==0:
                print("*",end=" ")
            elif j==0 or j==row-1:
                print("*",end=" ")
            else:
                print("*")
        print()
pattten3(10,10)