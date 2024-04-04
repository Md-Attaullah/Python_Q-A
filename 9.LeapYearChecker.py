Year = int(input("Enter the year :"))

if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0) :
    print(Year,",Its a Leaf Year")
else:
    print(Year,",Its Not a Leaf Year")