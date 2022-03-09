num = int(input("Print the number so that pattern will have that much rows\n"))
boolean = int(input("Enter the Number 0 or 1 to type cast into True or False \n"))
sys = str(bool(boolean))

if sys == 'True':
    print("You can start printing pattern")
    # outer loop to handle number of rows
    for i in range(0,num):   # for i in range(0, 3):
        # inner loop to handle number of columns
        # values is changing according to outer loop
        for j in range(0,i+1):
            print("* ", end="")
        print()
if sys == 'False':
    print("Bool is false printing pattern up side down")
    for i in range(num+1,0,-1):   # for i in range(0, 3): decrement the value by 1
        # inner loop to handle number of columns
        # values is changing according to outer loop
        for j in range(0,i-1):
            print("* ", end="")
        print()
#
# Left triangle star pattern
# n = 5
# for i in range(1, n+1):
#     # internal loop run for i times
#     for k in range(1, i+1):
#         print("*", end="")
#     print()
