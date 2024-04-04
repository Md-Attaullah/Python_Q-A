Fruit = str(input("Which Fruit Have :")) 


if Fruit == "Banana" or Fruit == "Pinapale" or Fruit == "banana" or Fruit == "pinapale":
    print
else:
    print("We Dont have the data of the",Fruit) 
    exit()

Colour = str(input("What is the Colour Of the Given Fruit :"))

if Fruit == "Banana" or Fruit == "Pinapale" or Fruit == "banana" or Fruit == "pinapale":
    if Colour == "Green" or Colour == "green":
        print(Fruit,"is Unripe")
    elif Colour == "Yellow" or Colour == "yellow":
        print(Fruit,"is Ripe")
    elif Colour == "Brown" or Colour == "brown":
        print(Fruit,"is OverRipe")
