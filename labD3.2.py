#q1

my_dictionary = {"Amal" : 1111111111, "Mohammed": 2222222222, "Khadijah" : 3333333333, "Abdullah": 4444444444, "Rawan" : 5555555555, "Faisal": 6666666666, "Layla" : 7777777777}

x = (input("enter the phone number: "))

if len(x) == 10 and x.isdecimal: 
    
    con = int(x)
    if con in my_dictionary.values():
        print(list(my_dictionary.keys())[list(my_dictionary.values()).index(con)])      
 
    else:
         print("Sorry, the number is not found")   

else:
   print("This is invalid number") 

#q2

def zero_list(listt):
    new_list = [num for num in listt if num != 0] + [num for num in listt if num == 0]
    return new_list

num_list = [1,4,0,6,0,3,5]

rearranged_zeros = zero_list(num_list)
print(rearranged_zeros)