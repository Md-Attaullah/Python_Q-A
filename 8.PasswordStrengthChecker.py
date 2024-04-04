Password = str(input("Enter the Password :"))

if len(Password) < 6:
    print("Weak Password")
elif len(Password) < 10:
    print("Medium Password")
elif len(Password) > 10:
    print("Strong Password")