Fruit = str(input("Which Fruit Have :")).upper()


if Fruit == "BANANA" or Fruit == "PINAPALE":
    print
else:
    print("We Dont have the data of the",Fruit) 
    exit()

Colour = str(input("What is the Colour Of the Given Fruit :")).upper()

if Fruit == "BANANA" or Fruit == "PINAPALE":
    if Colour == "GREEN":
        print(Fruit,"is Unripe")
    elif Colour == "YELLOW":
        print(Fruit,"is Ripe")
    elif Colour == "BROWN":
        print(Fruit,"is OverRipe")
