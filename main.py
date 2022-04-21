#Q1

my_contact = {"1111111111":"Amal",
            "2222222222":"Mohammed",
            "3333333333": "Khadijah",
            "4444444444" : "Abdullah",
            "5555555555": "Rawan",
            "6666666666" : "Faisal",
            "7777777777":"Layla"}


def contact_number (phone:str):
    if len(phone) > 10 or len(phone)<10 and int(phone):
       print("This is invalid number" +phone)
       return
    if phone in my_contact:
        print("the owner phone is {}".format(my_contact[phone])) 
    else:
        print("Sorry, the number is not found")
    
        
contact_number(input("Enter the number phone number"))
'''
contact_number("7777777777")
contact_number("7777777788")
contact_number("777777778A8")
contact_number("777777778888")
contact_number("2222222222")
'''


#Q2
def sort_num (new_list:list):
   return sorted(new_list)

list_n = [4, 4, 4, 5,5,1,2,2,3,7,6]
print(sort_num(list_n))
