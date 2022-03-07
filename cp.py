print("what is your age ? Age will be considered  from (7-100)")
ag = input()
age = int(ag[:3])
if age >= 7 and  age <= 100:
    print(f"Entered age {age} is between 7-100. We will check further")
    if age < 18:
        print(f"Age  {age} < 18. You can not drive")
    if age == 18:
        print(f"Age  {age}=18 .We will think about it")
    if age > 18:
        print(f"Age {age} > 18. Congrats !! You can drive")
else:
    print("License will not be issued as eligible age is from 7-100")
