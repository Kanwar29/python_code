a=[]
n=int(input("Enter the size of the array:"))
for x in range(n):
    print(f"Enter the number you wish to enter:")
    x=int(input())
    a.append(x)
l=a[0]
s=a[0]
for i in range(n):
    if a[i] > l:
        l = a[i]
    if a[i] < s:
        s =a[i]
print(f"Largest number in array is :{l}")
print(f"smallest number in array is : {s}")

