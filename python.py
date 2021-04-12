#  __init__ function is called a constructor, or initializer, and is automatically called when you create a new instance of a class.

# Tuples have structure, Lists have order.



# Python has five standard data types -
	
Numbers
String
List
Tuple
Dictionary


# clear Screen -> import os -> os.system(‘cls’) /windows


# Number:

 8+2*10 	= 28
(8+2)*10 	= 100

 18/4 	= 4.5
 18 // 4	= 4
 
 5*5*5		= 125
 5 ** 		= 125

 Tuna=10
 Tune=20  
 Sum=Tuna+Tune
 30



# String:

 Name= ’faiz’
 Name * 5  -> faiz faiz faiz faiz faiz




# Slicing up String:

 name=’bangladesh’
 name[2]   -> n
 name[2:5] -> ngl
 name[:5] ->  bangl 
 name[5:] ->  adesh

 len(name) | len(“bangladesh”)





# Lists:

 players=[21,23,25,27,29]
 players[3] -> 25
 players[3] = 52
 players + [31,33,35,37,39]   //this is added temporarily
 players.append(31) //this is added permanently
 players.append[1] = [] //delete items permanently
 players[:]=[]

# If Elif Else:    

 age=13

if age < 21:
    print('No beer for you!!!')

name='faizxn'
if name is 'faiz':
    print('Whats up Faiz.. How r u?')

elif name is 'suma':
    print('Whats up Suma!!!')

else:
    print('Pls!! do sign up')


# For:
 
foods=['banana', 'mango', 'jackfruit', 'coconut']

for food in foods:
    print(food)
    print(len(food))


# Range and While:
 
for x in range(100):
    print(x)


for x in range(100):
    print('Faiz')

for x in range(5, 10):
    print(x)

for x in range (10, 500, 50):    //50 used for distance number
    print(x)

numbers=5

while numbers < 10:

    print(numbers)

    numbers +=1


 
# Comment & Break:

 ‘’’’’’    #   -> Comment

magicNum = 6

for n in range(101):
    if n is magicNum:
        print(n, ' is the magic number..!!')
        break
    else:
        print(n)


 # Continue:

numbersTaken=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20,99]
print('Here are the number that are still available: ')

for n in range (1, 100):
    if n is numbersTaken:
        continue
    print(n)


 
# Functions: 
  
 def beef():
    print('Dayum! functions are cools ')

 def bitcoin_to_usd(btc):
    amount = btc * 10
    print(amount)

beef()
bitcoin_to_usd(10)


# Returns Value:

 def allow_dating_age(age):
    girls_age = age/2+7
    return girls_age

buckys_limit = allow_dating_age(35)
creepy_limit = allow_dating_age(53)

print('Buckys can date girls', buckys_limit, 'or olders')
print('Creepys can date girls', creepy_limit, 'or olders')








#Default value for arguments: 
 
  def get_gender(sex='unknown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

get_gender('m')
get_gender('f')
get_gender()


#Variable Scope:

>> Local variable | Global Variable


#Keyword Argument:

 def dump_sentence(name='tuna',action='ate',item='mango'):
    print(name, action, item)

dump_sentence()
dump_sentence(name='faiz')
dump_sentence(name='suma', action='burger')


#Flexible Number for Arguments:
 
 def add_num(*agrs):
    sum=0
    for a in agrs:
        sum +=a
    print (sum)

add_num(3)      -> 3
add_num(3,6,9)  -> 18


#Unpacking Arguments:

def users(name, age, id):
    print(name, age, id)

user_data=['faiz', '27', '705030']

users(*user_data)







#My trips to Walmart and Sets

 grocearies = {'milk', 'mango', 'mango', 'beer', 'vodka', 'lotion'}
print(grocearies)

if 'milk' in grocearies:
    print('You already have mill hoss!!!')

else:
    print('Oh yea! you need milk')

 


#Dictionary:
 
Tony -> Key
Cool but smells -> Values


classmates = {'Tony':'cool but smells', 'Emma': 'Sits beside me', 'Lucy': 'Aks too   many questions'}
print(classmates)

for k,v in classmates.items():
    print(k+v)


#Modules:

Page: method.py

 
	def name():
  print('Bangladesh University')

Page: main.py


  import method
  method.name()










# Download image from Web:

 import random
 import urllib.request

 def download_web_img(url):
    name = random.randrange(1,100)
    fname = str(name)+'.jpg'
    urllib.request.urlretrieve(url, fname)

download_web_img('https://facebook.com/zuck/photos/20042112.jpg')





# How to read and write files:
 
#Write_Text_Files

fw=open('sample.txt', 'w')
fw.write('Bangladesh University \n')
fw.write('Department name is Computer Science and Technology \n')
fw.write('ID number of students is 201311035110')
fw.close()

#Read_Text_Files

fr=open('sample.txt', 'r')
text= fr.read()
print(text)

# Download Files from Web Sites:

 from urllib import request
goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GooG&d'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r'goog.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()

download_stock_data(goog_url)



# Web Scraping with Beautiful-Soup: 


# You are the only exception 

 name=input('whats ur name? \n')
 print('Hello '+name)

 name=int(input('whats ur name? \n'))
 print(name)

 
while True:
    try:
        number = int(input('whats ur fav number? \n'))
        print(number)
        break
    except ValueError:
        print('Make sure and enter a number')

----------

while True:
    try:
        number = int(input('whats ur fav number? \n'))
        print(number)
        break
    except ValueError:
        print('Make sure and enter a number')
    except ZeroDivisionError:
        print('Dont peak zero')
    finally:
        print('loop complete')



# Classes and Object:

 class Enemy:
    life=3

    def checklife(self):
        print('Bangladesh University')

ojb_enemy = Enemy()
ojb_enemy.checklife()


# Init:

class MagicMethod:

    def __init__(self):
        print('Bangladesh University')

    def faiz(self):
        print('My name is Faiz')

magic_method = MagicMethod()
magic_method.faiz()


		Bangladesh University
My name is Faiz
  

# Class Variable vs Instance Variable 
 
 class Girl:
    gender = 'Female'
    def __init__(self,name):
        self.name = name

s = Girl('Suma')
f = Girl('Farzana')

print(s.name)
print(f.name)
print(s.gender)


# Inheritance:

 class Parent:

    def print_last_name(self):
        print('Suma')

class Child(Parent):

    def print_first_name(self):
        print('Akter')

obj = Child()
obj.print_first_name()
obj.print_last_name()





# Multiple- Inheritance:

 //pass used to pass multiple class in inheritance 

class Mario():

    def move(self):
        print('I am moving')

class Shroom():

    def eat_shroom(self):
        print('I am now too big')

class BigMario(Mario, Shroom):
    pass

obj=BigMario()
obj.move()
obj.eat_shroom()


 # Threading

 import threading

# Using threads allows a program to run multiple operations concurrently in the same process space!!!

class MyMessenger(threading.Thread):
     def run(self):
         for _ in range(10):
             print(threading.current_thread().getName())

x = MyMessenger(name='Send out message')
y = MyMessenger (name='Receive Message')

x.start()
y.start()


 # Word_Frequency_Counter:

 




# Bit Wise Operator:

 
#Binary AND

a = 50    #110010
b = 25    #011001
c = a & b #010000
print(c)

16


# Finding largest or Smallest items:

 import heapq

grades=[32,43,567,34,24,546,95]
print(heapq.nlargest(5,grades))

stocks=[
    {'tikcer':'Google','Price':201},
    {'ticker':'Facebook','Price': 202}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))


# Dictionary Calculations:

 


# Sorting Custom Object:

 from operator import attrgetter

class User:
    def __init__(self,x,y):
        self.name=x
        self.user_id=y

    def __repr__(self):
        return self.name + ' : '+ str(self.user_id)

users = [
    User('Suma',43),
    User('Farzana', 13),
    User('Tamanna', 23),
    User('Amanda', 32)
]
for usr in users:
    print(usr)

print('-------------------')
for usr in sorted(users, key=attrgetter('name')):
    print(usr)

print('-------------------')
for usr in sorted(users, key=attrgetter('user_id')):
    print(usr)

