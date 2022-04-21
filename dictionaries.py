phoneBook ={
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla",
}

checkStatus = False


while checkStatus == False:
    phoneNumber = input("Enter Phone Number ")
    if len(phoneNumber) == 10 and phoneNumber.isdecimal:
        if phoneNumber in phoneBook :
            print(phoneBook[phoneNumber])
            checkStatus = True
        else:
            print("Sorry, the number is not found")
    else:
        print("This is invalid number")
        
        