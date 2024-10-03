a=5
b=10
for i in range(a):   #0,1,2,3,4
    for j in range(b): #0,1,2,3,4,5,6,7,8,9
        if i==0 or i==a-1 or j==0 or j==b-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()