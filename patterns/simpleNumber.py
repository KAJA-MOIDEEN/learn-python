rows = 10
colums = 10
def call(rows,colums):
    for i in range(0,rows+1):
        for j in range(0,colums+1):
            if i==0 or j==colums:
                print(j, end=" ")
            elif i==5 and j==5:
                print("*", end=" ")
            elif i==j and j==i:
                print(i, end=" ")
            elif i==rows or j==0:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()
call(rows,colums)