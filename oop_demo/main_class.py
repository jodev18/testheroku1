
from Plant import Plant


pl = Plant()

inputx = input("1. Water\n2.Wilt\n3.Get flower\n4.Get fruit")

while inputx != 'q':
    
    inputx = input("1. Water\n2.Wilt\n3.Get flower\n4.Get fruit")

    if inputx == "1":
        print("Growing plant.")
        pl.water_plant()
        continue
    elif inputx == "2":
        print("Wilting plant.")
        pl.wilt_plant()
        continue
    elif inputx == "3":
        inputdate = input("Enter a date separated by dashes (1-11-2022):")
        flower = pl.get_flower(inputdate)
        if flower is not None:
            print(flower)
        continue
    elif inputx == "4":
        inputdate = input("Enter a date separated by dashes (1-11-2022):")
        fruit = pl.get_fruit(inputdate)
        if fruit is not None:
            print(fruit)
        continue