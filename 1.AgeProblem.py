Age = int(input("Provide the age :  "))

if Age < 13:
    print("This is Child")
elif Age < 19:
    print("This is Teenager")
elif Age < 60:
    print("This is Adult")
else:
    print("This is Senior")