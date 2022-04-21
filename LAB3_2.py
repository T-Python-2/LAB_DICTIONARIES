##Build a phone book program that receives the phone number, and returns the name of the owner.
'''
If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
If the number is less or more than 10 numbers, print "This is invalid number".
If the number contains letters or symbols, print "This is invalid number".
'''

phone_book = {"A1":1111111111,"A2":2222222222,"A3":3333333333,"A4":4444444444,}
def check_number(num):
    if len(num) != 10:
        print("This is invalid number")
        return
    elif not num.isnumeric:
        print("This is invalid number")
        return
    for name in phone_book:
        if phone_book[name] == int(num):
            print(name)
            return
    print("Sorry, the number is not found")


check_number(input("Enter phone number: "))












##Write a function that receives a list containing different numbers, rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.
def moveZeroes():
    nums = [1,0,2,0,3,0,4,0]
    result = [n for n in nums if n != 0]
    result.extend([0] * nums.count(0))
    print(result)
moveZeroes()