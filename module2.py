#Variables

full_name= "Neo Phukubye"
print(full_name)

first_name= "Neo"
surname="Phukubye"

full_name= "Neo Mashigo"
print(full_name)

#variables for strings,booleans and numbers

#assigning a string variable
string1="This is a string in double quotation marks"
string2='This is a string in single quotation marks'
string3="""We can have
multi line string in three
quotation marks!"""
string4='''we can also have
a multi line string in three 
single quotation mark!'''

print(string1)
print(string2)
print(string3)
print(string4)

#assigning a number variable
integer_variable= 1
float_variable= 1.0
print(integer_variable)
print(float_variable)

#assigning a boolean variable
is_raining=False
is_raining=True
print(is_raining)

# arithmetic operation




#addition
result= 5 + 3
print(result)
#subtraction
result1= 10-4
print(result1)
#multiplication
result2= 2*6
print(result2)
#division
result3=20/4
print(result3)
#integer division
result4=20//7
print(result4)
#modulus
result5=20%3
print(result5)

#string formatting= format()
name3= "Neo"
age2= 24
message= "My name is {} and I'm {} years old".format(name3, age2)
print(message)
#string formatting = fstrings
message1=f"My name is {name3} and I'm {age2} years old"
print(message1)

#creating a list

my_list= ["apple", "plum", "banana"]
print(my_list)

numbers= [ 10, 5, 2]

ages= [50, 25, 15]
print(ages)

mixed_list= ["Neo", 24, "Phukubye", 50, "Mashigo", 53 ]
print(mixed_list)

#print each element to the console
print(my_list[0])

#add, replace and remove items in list

#add items with append,insert and extend
fruits= ["apple", "plum", "cherry"]
fruits.append('orange')
print(fruits)

fruits.insert(1,"banana")
print(fruits)

fruits.extend(["banana","cherry","pineapple"])
print(fruits)

#remove items from a list with clear,remove,pop
fruits.pop()
print(fruits)

fruits.remove("banana")
print(fruits)

# fruits.clear()
# print(fruits)

#replacing items by using indexing
print(fruits)
fruits[2]="pear"
print(fruits)

#we can use list slicing to get sublists
fruits_sublist=fruits[0:3]
print(fruits_sublist)

#we can also use an optional step argument
fruits_sublist_step=fruits[0::2]
print(fruits_sublist_step)