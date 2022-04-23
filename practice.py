# Create a new dictionary : 
myFirstDictionary = {"name" : "Lama" , "file_no": 124}

# Access an element in a dictionary : 
print(myFirstDictionary["file_no"])

# Add a new element to the dictionary (best practice): 
myFirstDictionary["age"] = 23
print(myFirstDictionary)

'''
if the new key is already exist it will be modified to the new value
'''

# Add a new elements to the dictionary using update 
myFirstDictionary.update(height = 160 , weight = 48 )
print(myFirstDictionary)

# Another way => 
myFirstDictionary.update([["phone_num" , 0000] , ["birthday" , "29April"]])
print(myFirstDictionary)



# To check if a key is exist in a dictionary => 
if "name" in myFirstDictionary : 
    print("the key is found !")


# Delete an element from dictionary => 
del myFirstDictionary["phone_num"]
print(myFirstDictionary)

# To pop an item and get the value from dictionary =>
poped = myFirstDictionary.pop("file_no")
print(poped)


# To loop through a dictionary keys  =>
for key in myFirstDictionary: 
    print(myFirstDictionary[key])

