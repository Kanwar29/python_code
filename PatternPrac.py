n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()


n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print()

n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(n+1,1,-1):
    for j in range(1,i):
        print(j, end="")
    print()

n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(n,0,-1):
    for j in range(n,n-i,-1):
        print(j, end="")
    print()

n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<=5:
            print(" ",end="")
        else:
            print("*",end="")
    print()


n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

number=1
n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(1,n+1):
    for j in range(1,i+1):
        #print(j,end="")
        print(number,end=" ")
        number=number +1


n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(1,n+1):
    for j in range(1,n-i):
            print(" ",end="")
    for k in range(1,i+1):
        print("* ",end="")
    print()

n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(1,n+1):
    for j in range(1,n-i):
            print(" ",end="")
    for k in range(0,2*i-1):
        print("*",end="")
    print()


n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(n,0,-1):
    for j in range(1,n-i):
            print(" ",end="")
    for k in range(0,2*i-1):
        print("*",end="")
    print()

I = 65
for i in range(1,6):
    I = 65
    for j in range(1,i+1): #i is not refereshed hence next value start from 66-B then 67-c as loop runs for 1=1,2
        print(chr(I),end="")
        I=I+1
    print()

n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64 + j),end=" ")
    print()

n=int(input("Enter the no of rows you want to display:- \n"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64 + i),end=" ")
    print()
