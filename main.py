## Q1:Build a phone book program that receives the phone number, and returns the name of the owner. 

from typing import List


phone_book = {1111111111: "Amal" , 2222222222:"Mohammed",3333333333: "Khadijah", 4444444444:"Abdullah" ,5555555555:"Rawan" ,6666666666:"Faisal",7777777777:"Layla"}

print ("Please enter  a phone number")
phone_number = input()

#If the number is less or more than 10 numbers, print "This is invalid number".
#If the number contains letters or symbols, print "This is invalid number".

if len(phone_number) !=10 and phone_number.isdigit:
    print("This is invalid number")
else:

# If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
    for key , value in phone_book.items():
       if key ==  int(phone_number):
        print("The phone number owner is :"+value)
        break
    else:
        print("Sorry, the number is not found")

# Q2:Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

def arrange_list(number_list:list):
    for number in number_list:
        if number == 0:
            number_list.remove(number)
            number_list.append(number)
    return number_list

print(arrange_list([4,5,6,7,0,7,0,5]))



