# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 16:23:10 2020

@author: PC
"""

print("Hello Python")
print("Hello Python")

print("Ankit " + "Mistry")

myname = input("What is your name : ")
print("Your name is " + myname)

'''
int 23, 3, 0 -6 
float 2.6 -0.67 0 23.0
complex 3 +7j

bool True False

string str "Hello" 'hello'

list tuple set dict
'''

#integer float

2 45 -5
22.3 -5.8

3 + 6
3.0 + 6
2 - 6
3 * 4
12 / 5
12 // 5
3 ** 5
12 % 5

type(12/5)

type(2.1 + 6)

type(2.0)


3 + 4 * 2

(3 + 4) * 2

2 // 0.6 + 3 * 5

round(2.6)
round(-2.6)

abs(5)

import math
dir(math)
math.factorial(6)

math.sin(34)

# Variable

bucket <- water

bucket = "water"
bucket

age = 27
print(age)

_age = 23

2age = 23

Age = 32

age
Age

age2 = 34
a2ge = 21

age-23 = 34
age_23 = 90


my_age = 28
bro_age = my_age + 5
sis_age = my_age - 2

my_age, bro_age, sis_age = 20, 30, 25

myage = 28 # in 2020
myage = myage + 1

myage *= 2 
myage = myage * 2


var1 = 'hello'
var2 = "hello"

#"hello'

rain = "It 's \n \"outside\" \t\tRaining"
print(rain)

multiline = '''
    This is 1st
    This is 2nd
    3rd
'''
print(multiline)


var1  = "Hello"
var2 = " Python"

print(var1 + var2 + " I Love Python")

print("My age is " + str(5) + " years.")


age = 12
name = "Ankit"
print(f"My age is {age} year and My name is {name}")

print("My age is {} year and My name is {}".format(age, name))


quote = "I love python"

quote.upper()
quote.lower()
quote.find("I")
quote.count("o")
quote.capitalize()
quote.startswith("i")
quote.replace("love", "like")


quote = "I love"

'''
-6 I : 0
-5   : 1
-4 l : 2
-3 o : 3
-2 v : 4
-1 e : 5
'''

quote[-6]

quote[start : stop :step]
quote[2:5]
quote[0:]
quote[2:]
quote[:3]
quote[-4:-2]

quote[0::2]
quote[::-1]


quote = "I love"

quote[0] = "U"

quote + " You"

is_smiling = True

type(is_smiling)

is_smiling = False

True & True
|
~True


bin(34)

quote = "I love"
len(quote)
dir(quote)

id(quote)
id(is_smiling)

max(3,4,5,100)

pow(2, 6)

sum(1,2,3)





int(12)
int(12.5)
int("12")
int("gof")


float(12)
float(12.5)
float("12.5")


str(12)
str(12.5)
str("gof")


bin(1000)

hex(1000)

oct(1000)


# LIST

l1 = [2, 3, 8, -1, 9]
type(l1)

l2 = [23, 4.5, -67, True, "Hello"]
l2

l3 = [2, ["a", "b", "c"], True]

[ [1,2,3], [2,3,4], [4,5,6] ]


l2 = [23, 4.5, -67, True, "Hello"]
      0    1    2     3     4
      
l2[2]
l2[4]

l2[-1]
l2[-3]

l2[start:end]

l2[1:3]
l2[2:]
l2[:2]


l1 = [2, 3, 8, -1, 9]

l1.append(100)
l1

l1.extend([200,300,56])

l1.insert(3, 50)

l1.pop()

l1.remove(9)

l1.count(50)

l1.index(8)

l1.clear()

l1.reverse()

l1.sort()

len(l1)


x1, x2, x3 = ["I", "Love", "Python"]

" ".join(["I", "Love", "Python"])
",".join(["I", "Love", "Python"])

comma = ";"
comma.join(["I", "Love", "Python"])


# Tuples

t1 = (2,3,56, True, "Hello")
type(t1)


t1[1] = 100

t1[2:4]

t1.index(True)

t1.count(3)

120 x 80

#Set

s1 = set([3,4,5,7, 4])
type(s1)

s1.add(3)
print(s1)

s1.add(30)
print(s1)

s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])

s1.difference(s2)
s1.difference_update(s2)

print(s1)


s1.intersection(s2)

s1.issubset(s2)
s1.issuperset(s2)

s1.union(s2)

s1.pop()
s1

s1.remove(5)
s1

# Dictionary

[555, 444, 111]
John  Alice Bob

phonebook = {
 "John" : 555,
 "Alice" : 444,
 "Bob" : 111
}

dict(John=555,  Alice=444, Bob=111)

phonebook["John"]
phonebook["bob"]
phonebook["Jony"]

phonebook.get("John")
phonebook.get("Jony")

phonebook.keys()

phonebook.values()

for phone in phonebook.items():
    print(phone[0], phone[1])
    
    
phonebook.pop("John")

phonebook["John"] = 000

phonebook["Alice"] = 777

"Alice" in phonebook.keys()

"Alice1" in phonebook

555 in phonebook.values()
111 in phonebook.values()


phonebook = {
 456 : 555,
 "Alice" : 444,
 True : 111
}

phonebook[True]



True False



phonebook["John"]
phonebook["Bob"]
phonebook["Alice"]

#conditional logic

name = "John"

name == "John"
name == "John1"

name ="Alice"

if name == "John":
    print(phonebook["John"])
elif name == "Alice":
    print(phonebook["Alice"])
else:
    print(phonebook["Bob"])



if name == "John":
    print(phonebook["John"])
else:
    print(phonebook["Alice"])
    
name ="John"
print(phonebook["John"]) if name == "John" else print(phonebook["Alice"])


age = 0

if "":
    print("You are alive")
else:
    print("You are not yet born")
    
    
bool(21)
bool(0)

bool(0.1)

bool("Hello")

bool(" ")
bool("")

bool(True)


bool([0,0,0])
bool([])

and or not ==  > < >= <=


True and False

False or False

not ""

23 and 32


3 < 4

4 == 4
4 >= 5
 
 
((3 > 6) and (name == "Alice")) or (4 == 5)

False and (((3 > 6) and (name == "Alice")) or (4 == 5))

True or (((3 > 6) and (name == "Alice")) or (4 == 5))


age = 21
id(age)

2 == 2 
"Hello" == "Hello"
"Hello" == "hello"
True ==  True
2.5 == 2.5
[1,2,3] == [1,2,3]
[] == []

is

2 is 2 
"Hello" is "Hello"
"Hello" is "hello"
True is  True
2.5 is 2.5
[1,2,3] is [1,2,3]
[] is []

l1 = [1,2,3]
l2 = [1,2,3]
l1 is l2


id("Hello") is id("Hello")


print("Hello")


=  Ankit -: Hello Ankit
=  Python -: Hello Python

def my_2nd_fun(name):
    print("Hello "+ str(name))
    

my_2nd_fun("Ankit")

my_2nd_fun("World")

my_2nd_fun(23)


def print_hello():
    print("Hello")

print_hello()
'''
default args
keyword args
positional args
'''


def student_fun(sname,  grade, roll_no=45):
    print("Hi "+ str(sname) + ". Your number is "+ str(roll_no))
    print("Grade is "+ str(grade))
    
student_fun("Ankit", 56)

student_fun(roll_no=56, sname="Ankit")

student_fun("Ankit" , 12, 44)


def add_num(num1, num2):
    return num1+num2

sum1 = add_num(3, 4)

def is_even(num):
    '''
    This function return True if even number passed else False.
    '''
    if num % 2 == 0:
        return True , "True"
    else:
        return False, "False"


even, even1 = is_even(40)


help(print)
print(print.__doc__)

is_even.__doc__
help(is_even)



print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

#for while:

range(5)

for i in range(10000):
    print(i, "Hello")
    
my_list = [34, 67, 8.9, "Hello"]

for item in my_list:
    print(item)

phonebook = {
 "John" : 555,
 "Alice" : 444,
 "Bob" : 111
}


for item in phonebook.items():
    print(item[0],  item[1])
    #print(item)

for i in range(5):
    print(i, "Hello")

for item in my_list:
    print(item)

for key, val in enumerate(my_list):
    print(key, val)


for i in range(5):
    print(i)
    
i = 0   
while i < 5:
    print(i, "Hello")  
    i += 1

#continue break pass
    my_list 
    
    
for item in my_list:
    if item == 8.9:
        break
    print(item)

def smile_detection():
    pass







    
    
    
    

