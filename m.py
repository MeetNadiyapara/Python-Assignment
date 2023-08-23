
'''
print("This is 'Python'")
print("This is \n'Python'")
print("This is \t'Python'")
print("This is 'Py\bthon'")
print("This is 'Python'",end="")
print("This is the 'Python'")
print("This","is","Python",sep="2")
#print("This is the 'Python'")
print("hii","hello",sep=".")


str="    Hello World"

print(str[-1])
print(str[0:5])
print(str[:-1])
print(str[5:])
print(str.strip())
print(str.lower())
print(str.upper())
print(str.replace("Hello","Hii"))
print(len(str))

print(str.capitalize())
print(str.casefold())
print(str.count("h"))
print(str.endswith("/"))
print(str.startswith("/"))
print(str.find("hello"))
print(str.index("hello"))
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isupper())
print(str.title())

name=10
name2=20
print(name+name2)

m="meet"

print(R"my name is",m)
name=20

e=55j

print(type(e))

a=55.46

print(int(a))

x=55

print(float(x))

a=int(input("enter :"))

b=int(input("enter :"))

print(a)

print(b)
print("sum",a+b)


fnm=input("enter")
lnm=input("enter")

print(fnm+" "+lnm)


str="hi hello"
print(str.split())


id=34
name='meet'

print(f"id is {id} and name is {name}")

sub1=int(input("Enter Python:"))
sub2=int(input("Enter C/C++:"))
sub3=int(input("Enter JAVA:"))

if sub1>40 and sub2>40 and sub3>40:

    total=sub1+sub2+sub3
    print("Total:",total)

    pr=total/4
    print("Percentage:",pr)

    if pr<=70:
        print("First Class")

    elif pr<=60:
        print("Second Class")

    elif pr<=50:
        print("Third Class")

    elif pr<=40:
        print("Fail")

else:                               
    print("The Result is Fail")




m="My Name Is Meet"

print(m.split("I"))


for i in "My Name Is Meet":
    print(i)

 
for i in range(6):
    for j in range(i):
        print(i,end=" ")
    print(" ")

a=0

while a<11:
    print(a)
    a+=1
    if a==5:
        break

for i in range(1,11):
    if i<6:
        continue
    print(i)

for i in range(1,11):
    pass
    

i=["1hii","3hello","2hey"]
m=0
print(i.index("hii"))
i[0]="Heyy"
print(i)

for j in i:
    print(f"Index of list {i.index(j)} And List {i}")

if "hey" in i:
    print("Yes")
else:
    print("No")

print(len(i))

i.append("HUY")
i.insert(2,"Heyya")
i.remove("Heyya")
i.pop()
i.clear()

del i[1]


j=i.copy()
print(i)
print(j)

j=['hi','hello','huyy']

print(i+j)
j.extend(i)
print(j)

i.reverse()
i.sort()
print(i)

j=[input(":")]
print(j)


i=("Hii","Hello","Huyy")

print(i[0])

print(len(i))

del i

print(i)

i={25,52,65,56,98,74}


if 25 in i:
    print("Yes")

else:
    print("No")

for i in i:
    print(i)

i.add(85)
i.update([45,66,11])
i.remove(56)
i.pop()

print(i)
j={565,56,741,963}
print(j)

x=i.union(j)
y=i.intersection(j)
print(x,y)

i={'Meet':215,"Nidhi":852}
print(i.get('Meet'))
print(i['Nidhi'])
i['Meet']=456
for i in i.values():
    print(i)

for i in i.items():
    print(i)
    

for m,j in i.items():
    print(f"Key={m} And Value={j}")

i['Krishna']=951
print(i)

if 215 in i.values():
    print("Yes")
else:
    print("No")

print(len(i))

i.pop('Meet')
del i['Meet']
del i

j=i.copy()
print(j)


def meet():
    print("Hii")

def meet1(a,b):
    print("Sum",a+b)

meet()
meet1(25,65)

city=''
salary=0

def company():
    city=input("Enter:")
    salary=int(input("Enter:"))

    print("city is",city)
    print("salary is",salary)

company()

def company(city,salary):
    print("City:",city)
    print("Salary:",salary)

city=input("City:")
salary=input("Salary:")

company(city,salary)


def school(rno,clas,div='c'):
    print("rno:",rno)
    print("Class",clas)
    print("Div",div)

school(52,'A')    


def school(rno,clas,div='c'):
    print("rno:",rno)
    print("Class",clas)
    print("Div",div)

school(rno=52,clas='A',div='A')

def picture(*information):
    print("Color",information[0])
    #print("Width",information[1])
    #print("Height",information[2])


picture('Green',456,852)

def company(city,salary):
    print("City:",city)
    print("Salary:",salary)

ci=input("City:")
sa=input("Salary:")

company(ci,sa)

def sum(a,b):

    return a+b

a=int(input("Enter A:"))
b=int(input("Enter b:"))
c=sum(a,b)
print(c)

def picture(information):
    print("Color:",information[0])
    print("Width:",information[1])
    print("Height:",information[2])


picture(['Green',456,852])

def picture(information):
    print("Color:",information['Col'])
    print("Width:",information['Wid'])
    print("Height:",information['Hei'])

picture({'Col':'Green','Wid':65,'Hei':95})
    
c=lambda a,b:a*b

#print(c(45,88))

def mul():
    print(c(45,88))
mul()


import m9a

m9a.inp

from m9a import inp
inp()

from m9a import*
inp()



from m9a as mm

mm.inp()


import random

a=random.random()
print(a)

b=random.randint(1000,9000)
print(b)

c=random.randrange(1000,9000,10)
print(c)
D=['India','UK','USA']
d=random.choice(D)
print(d)

random.shuffle(D)

print(D)

import math
                               
print(math.pi)
a=math.ceil(8523.23)
print(a)
b=math.floor(8523.23)
print(b)
c=math.factorial(5)
print(c)
d=math.pow(3,2)
print(d)
e=math.sqrt(25)
print(e)


open('file.txt','x')
open('file1.txt','a')
open('file2.txt','w')
a=open('file2.txt','w')
a.write('This File Is Create Using Write Mode')
a=open('file2.txt','a')
a.write("\n Hello")
a=open('file1.txt','a')

color=input("Enter Color Name")

height=input("Enter Picture Height")

width=input("Enter Picture Width")

a.write(f"The Picture Color Is{color},The Picture Height Is{height},And The Width Of Picture Is{width}")


a=open('file2.txt','r')
print(a.read())
print(a.readline())
print(a.readlines()[1])

a=open('file2.txt','r+')
a.write('\n Hii , Hello')
print(a.read())

import os
 
os.remove('file.txt')


a='Hii'
try:
    print(A)
except:
    print("Error Occur")
b='Hello'
print(b)



try:
    value1=int(input("Enter value:"))
    value2=int(input("Enter value:"))
    print("Sum",value1+value2)
except:
    print("Error Occured")



try:
    value1=int(input("Enter value:"))
    value2=int(input("Enter value:"))
    print("Sum",value1+value2)
 
except Exception as e:
    print(e)


try:
    value1=int(input("Enter value:"))
    value2=int(input("Enter value:"))
    print("Sum",value1+value2)

except Exception as e:
    print(e)

finally:
    value3=int(input("Enter Value:"))
    value4=int(input("Enter Value:"))
    print("Sum",value3+value4)

try:
    value1=int(input("Enter value:"))
    value2=int(input("Enter value:"))
    print("Sum",value1+value2)

except Exception as e:
    print(e)

else:
    value3=int(input("Enter Value:"))
    value4=int(input("Enter Value:"))
    print("Sum",value3+value4)


class picture:
    height=55
    width=52
    color='green'

    def flower(self):
        print("This Is Picture")

obj=picture()
print(obj.color)
print(obj.height)
print(obj.width)
obj.flower()



class picture:
    height=55
    width=52
    color='green'


    def photo(self):
        print("Picture Color:",self.color)
        print("Picture width:",self.width)
        print("Picture height:",self.height)

obj=picture()
obj.photo()



class picture:
    height=0
    width=0
    color=''

    def photodetail(self):
        self.color=input("Enter Color:")
        self.width=input("Enter width:")
        self.height=input("Enter height:")

    def photo(self):
        print("Picture Color:",self.color)
        print("Picture width:",self.width)
        print("Picture height:",self.height)

obj=picture()

obj.photodetail()
obj.photo()


class inherit:
    money=0
    property=0

    def detail(self):
        self.money=input("Enter Money:")
        self.property=input("Enter property:")

class inherit2(inherit):
    
    def data(self):
        print("Money:",self.money)
        print("Property:",self.property)


obj=inherit2()

obj.detail()
obj.data()
        


class a:
    nm=' '
    dob=0

    def data(self):
        self.dob=input("Enter Dob")
        self.nm=input("Enter Name")

class b:
    nm1=' '
    dob1=0

    def data1(self):
        self.dob1=input("Enter Dob1"
                        )
        self.nm1=input("Enter Name1")

class c:
    nm2=' '
    dob2=0

    def data2(self):
        self.dob2=input("Enter Dob2")
        self.nm2=input("Enter Name2")

class d(a,b,c):

    def detils(self):
        print("Dob",self.dob)
        print("Dob1",self.dob1)
        print("Dob2",self.dob2)
        print("Name",self.nm)
        print("Name1",self.nm1)
        print("Name2",self.nm2)


obj=d()
obj.data()
obj.data1()
obj.data2()
obj.detils()



class a:
    money=0
    car=0

    def data(self):
        self.car=input("Enter Car:")
        self.money=input("Enter Money:")

class b(a):

    property=0
    dimond=0

    def data1(self):
        self.property=input("Enter Property:")
        self.dimond=input("Enter Dimond:")

class c(b):

    def detail(self):
        print("------------------Class A-----------------")
        print("Cars",self.car)
        print("Money",self.money)
        print("------------------Class B-----------------")
        print("Property",self.property)
        print("Dimiond",self.dimond)

obj=c()
obj.data()
obj.data1()
obj.detail()



class polymor:

    def data(self,branch,state):
        print("Branch:",branch)
        print("State:",state)

    def data(self,contry,position):
        print("Country:",contry)
        print("POsition:",position)

obj=polymor()
obj.data('India',1)



class website:
    
    def login(self,id,name):
        print("Id:",id)
        print("Name",name)

class website1(website):

    def login(self, id, name):
        return super().login(id, name)
    
obj=website1()
obj.login(4004,'MN')


class picture:
    height=55
    width=52
    color='green'

    def flower(self):
        print("This Is Picture")

obj=picolorcture()
print(obj.)
print(obj.height)
print(obj.width)
#obj.flower()
obj.color='Purpole'
obj.height=79845
obj.width=13265
print(obj.color)
print(obj.height)
print(obj.width)

#print(picture().color)
#print(picture().height)
#print(picture().width)

#picture().color='Purpole'
#picture().height=7985
#picture().width=7985

#print(picture().color)
#print(picture().height)
#print(picture().width)


class a:
    __money=798798798465465465151650
    __car=7987984650

    def detail(self):
        print("money:",obj.__money)
        print('car:',obj.__car)


    def __data(self):
        print("This IS Function")

    def data1(self):
        self.__data()

obj=a()
#print("money:",obj.money)
#print('car:',obj.car)
obj.detail()
obj.data1()


import re
a='This is Python 09'
#print(re.search('is',a))
#print(re.match('is',a))
#print(re.findall('is',a))
#print(re.findall('[A-Z]',a))
#print(re.findall('[a-z]',a))
#print(re.findall('[0-9]',a))
#print(re.findall('[[A-Za-z0-9]',a))
#print(re.findall('^T',a))
#print(re.findall('09$',a))
#print(re.findall('\w',a))
#print(re.findall('\W',a))
#print(re.findall('\s',a))
#print(re.findall('\S',a))
#print(re.findall(r'\bThis',a))
#print(re.findall('09\B',a))
#print(re.findall('\AT',a))
#print(re.findall('09\Z',a))
#print(re.findall('\d',a))
#print(re.findall('\D',a))
#print(re.findall('Th..',a))
#print(re.findall('This|That',a))



b=input("Enter email-id: ")
c=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#c="[A-Z]+[a-z]+[0-9]+[.]+[@]+[_]+\S"
d=re.findall(c,b)

if d:
    print("Valid")
else:
    print("Invalid")


from tkinter import *

a=Tk()

mainloop()

'''


import tkinter

from tkinter import ttk

a=tkinter.Tk()

a.title("My App")

a.geometry("540x560")

a.config(bg='silver')

#tkinter.Label(text="User Name: ",bg='green',fg='white',font='Arial 17 bold italic').pack()
#tkinter.Label(text="Password: ",bg='green',fg='white',font='Arial 17 bold italic').pack()

#tkinter.Label(text="User Name: ",bg='green',fg='white',font='Arial 17 bold italic').place(x=0,y=0)
#tkinter.Label(text="Password: ",bg='green',fg='white',font='Arial 17 bold italic').place(x=0,y=37)

tkinter.Label(text="User Name: ",bg='silver',fg='white',font='Arial 17 bold italic').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Password: ",bg='silver',fg='white',font='Arial 17 bold italic').grid(row=1,column=0,sticky='w')

tkinter.Entry().grid(row=0,column=1)
tkinter.Entry().grid(row=1,column=1)

tkinter.Radiobutton(value=0,text="Male",bg='silver',fg='white',font='Arial 17 bold italic').grid(row=2,column=0,sticky='w')
tkinter.Radiobutton(value=1,text="Female",bg='silver',fg='white',font='Arial 17 bold italic').grid(row=2,column=1,sticky='w')

tkinter.Checkbutton(text="Python",bg='silver',fg='white',font='Arial 17 bold italic').grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text="Flutter",bg='silver',fg='white',font='Arial 17 bold italic').grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text="JAVA",bg='silver',fg='white',font='Arial 17 bold italic').grid(row=5,column=0,sticky='w')
tkinter.Checkbutton(text="Android",bg='silver',fg='white',font='Arial 17 bold italic').grid(row=6,column=0,sticky='w')

country=['USA','UK','INDIA']

ttk.Combobox(values=country).grid(row=7,column=0,sticky='w')

tkinter.Button(text="OK",bg='silver',fg='white',font='Arial 17 bold italic').place(x=265,y=299)

tkinter.mainloop()



