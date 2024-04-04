Distance =int(input("What is the Distance :"))

if Distance < 3:
    print("Walk")
elif Distance < 16:
    print("Bike")
elif Distance > 15:
    print("Car")