# Q1:Build a phone book program that receives the phone number, and returns the name of the owner.

from textwrap import indent
from tokenize import Number


number_book = {"Amal": 11111, "Mohammed": 22222, "Khadijah": 33333, "Abdullah": 44444, "Rawan":  55555, "Faisal":  66666, "Layla": 77777}


phone_num = int(input("Please enter the phone number : "))
# If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".

if len(str(phone_num)) != 5: 
        print("This is invalid number , must be 10")
elif str(phone_num).isnumeric() == False:
        print("This is invalid number !")
else:
    for i in number_book:
        if number_book[i] == phone_num:
            print(" The Owner : ", i)
            break
    else:
      print("Sorry, the number is not found !")

        

    
# Q2:Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

def arrangeList(num_list:list):
    for num in num_list:
        if num == 0:
            num_list.remove(num)
            num_list.append(num)
    return num_list

print(arrangeList([6 , 8 , 0, 3 , 0 , 4 , 0 , 2 , 4 , 0 , 5]))
