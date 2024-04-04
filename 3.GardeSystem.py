Score = int(input("Provide the Score :  "))

if Score > 100:
    print("Garde Can't Be more Than 100")
    exit()

if Score > 90:
    print("This is A Garde")
elif Score > 80:
    print("This is B Garde")
elif Score > 70:
    print("This is C Garde")
elif Score > 60:
    print("This is D Grade")
else:
    print("This is F Grade")