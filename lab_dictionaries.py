#Dictionary_LAB

#------------------------------------ Q1 ------------------------------------

phoneBook = {
    "Amal":1111111111,
    "Mohammed":2222222222,
    "Khadijah":3333333333,
    "Abullah":4444444444,
    "Rawan":5555555555,
    "Faisal":6666666666,
    "Layla":7777777777
    }

def check_the_number(number):
    if len(number) != 10:
        print("This is invalid number")
        return
    elif not number.isnumeric:
        print("This is invalid number")
        return

    for name in phoneBook:
        if phoneBook[name] == int(number):
            print(name)
            return
    print("Sorry, the number is not found")


check_the_number(input("Enter the number "))


#------------------------------------ Q2 ------------------------------------

def arrange(numberList:list):
    for number in numberList:
        if number == 0:
            numberList.remove(number)
            numberList.append(number)
    #numberList.sort(reverse=True)
    return numberList

print(arrange([4,5,6,7,10,12,20]))

