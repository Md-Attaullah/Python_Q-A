Coffee = str(input("What Size of Coffee You Want (Small/Medium/Large) :")).capitalize()

Extra_Shot =str(input("Do you Want Extra Shot (True/False) :")).capitalize()
print(Extra_Shot)

if Extra_Shot == True:
    print(Coffee,"Coffee with Extrashot of espresso")
else:
    print(Coffee,"Coffee ")