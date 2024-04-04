Age = int(input("Enter the Age :"))

Price = 12 if Age >= 18  else 8


Day =str(input("When Your wanted to book the Ticket :")).upper()

if Day =="WEDNESDAY":
    Price = Price-2

print(Price)