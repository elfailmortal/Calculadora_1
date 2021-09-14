#UNDERDEVELOPMENT
#BAJO DESARROLLO
from math import *
from cmath import *
from sys import *
import time

#user info
welcome = "Welcome to Memphis' calculator."
print(welcome)
name = input("Now, please write here your name: ")
print(str("Mmmm, {0} that is a very interesting name").format(name))
time.sleep(2)
print("Well I can do the following types of operations:","Basics","Angles","Even numbers on a range",sep='\n')
time.sleep(5)
election = input("Well now write down the number of the operation you want to do 1.-Basics,2.-Angles,3.-Evens,4.-Complex: ")
operations = []
operations_basics = ["1.-Sum","2.-Substraction","3.-Product","4.-Division","5.-Square root","6.-Power"]
operations_angles = ["1.- Find Hypotenuse","2.-Sum of angles","3.-Covert sexagesimal to radians","4.-Convert sexagesimal to centecimal ","5.-Torcional Angle","6.-Convert radians to Decimal","7.-Convert radians to Sexagesimal","8.-Convert decimal to sexagesimal","9.-Convert decimal to radians"]
operations_evens = ["1.-Even numbers in the range 0 to X","2.-Check if the number is even or odd"]
operations_complex = ["1.-Polare coordinates","2.-Sum","3.-Substraction","4.-Product","5.-division"]
recept_operations = []
result = 0
pi = math.pi
n1 = 0
n2 = 0
#define operations
def sum_bas(n1, n2):
    while True:
        n1 = input("Write your first number: ")
        n2 = input("Write your second number: ")
        try:
            val = int(n1)
            val2 = int(n2)
            result = n1+n2
            recept_operations.append(result)
            return result
        except ValueError:
            print("One of the inputs is not an integer, please rewrite them carefully")
            continue

def subs_bas(n1,n2):
    while True:
        n1 = input("Write your first number: ")
        n2 = input("Write your second number: ")
        try:
            val = int(n1)
            val2 = int(n2)
            result = n1-n2
            recept_operations.append(result)
            return result
        except ValueError:
            print("One of your inputs is not an integer, please rewrite them carefully")
            continue
def product_bas(n1,n2):
    while True:
        n1 = input("Write your first number: ")
        n2 = input("Write your second number: ")
        try:
            val = int(n1)
            val2 = int(n2)
            result  = n1 * n2
            recept_operations.append(result)
            return result
        except ValueError:
            print("One of your inputs is not an integer, please rewrite them carefully")
            continue
def division_bas(n1,n2):
    while True:
        n1 = input("Please write your first number: ")
        n2 = input("Please write your second number: ")
        result = 0
        try:
            n1/n2
            result = n1/n2
            recept_operations.append(result)
            return result
        except ZeroDivisionError as e:
            print("Error code:",e)
            continue
def square_root_bas(n1):
    while True:
        n1 = input("Please write your number: ")
        try:
            val=int(n1)
            result = n1**2
            recept_operations.append(result)
            return result
        except ValueError:
            print("One of the inputs you gave is not an integer, please rewrite them carefully")
            continue
def power_bas(n1,n2):
    while True:
        n1 = input("Please write your first number: ")
        n2 = input("Please write your second number: ")
        try:
            val = int(n1)
            val2 = int(n2)
            result = n1**n2
            recept_operations.append(result)
            return result
        except ValueError:
            print("One of the inputs you gave is not an integer, please rewrite them carefully")
            continue
def hypotenuse_ang(n1,n2):
    while True:
        n1 = input("Write your first angle without the °: ")
        n2 = input("Write your second angle without the °: ")
        try:
            val = int(n1)
            val2 = int(n2)
            result = str(int(round(math.degrees(math.atan2(n1,n2)))))+chr(176)
            recept_operations.append(result)
            return result
        except ValueError:
            print("One of the inputs you gave is not an integer, please rewrite them carefully")
            continue
def Sum_ang(n1,n2):
    while True:
        n1 = input("Write your first angle without the °: ")
        n2 = input("Write your second angle without the °: ")
        try:
            val = int(n1)
            val2 = int(n2)
            result = str(int(n1+n2))+chr(176)
            recept_operations.append(result)
            return result
        except ValueError:
            print("One of th inputs you gave is not an integer, please rewrite them carefully")
            continue
def sexa_to_radians(n1):
    while True:
        n1 = input("Write your sexagesimal degrees: ")
        try:
            val = int(n1)
            result = (n1*(pi/180))
            recept_operations.append(result)
            print(str("{0} sexagesimal degrees is equal to {1} radians").format((str(n1)+chr(176)),result))
            break
        except ValueError:
            print("The input you gave is not an integer, please rewrite it carefully")
            continue
def sexa_to_decimal(n1):
    minut = 0
    secs = 0
    while True:
        n1 = input("Write your sexagesimal degrees value: ")
        try:
            val = int(n1)
            minut = (n1*60)
            secs = minut * 60
            result = str("{0}° is equal to {1} minutes or {2} seconds").format(n1,minut,secs)
            recept_operations.append(result)
            return result
        except ValueError:
            print("The input you gave is not an integer, please rewrite it carefully")
            continue
class Torcional(n1):
    class Points(object):
        def __init__(self,x,y,z):
            self.x = x
            self.y = y
            self.z = z
        def __sub__(self,no):
            return Points((self.x-no.x),(self.y-no.y),(self.z-no.z))
        def dot(self,no):
            return((self.x*no.x)+(self.y*no.y)+(self.z+no.z))
        def cross(self,no):
            return Points((self.y*no.z-self.z*no.y),(self.z*no.x-self.x*no.z),(self.x*no.y-self.y*no.x))
        def absolute(self):
            return pow((self.x ** 2 + self.y ** 2 + self.z ** 2),0.5)
        poins = list()
        for i in range(4):
            a = list(map(float,n1.split()))
            poins.append(a)
        a,b,c,d = Points(*poins[0]), Points(*poins[1]), Points(*poins[2]),Points(*poins[3])
        x = (b-a).cross(c-b)
        y = (c-b).cross(d-c)
        angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
        print("%.2f"%math.degrees(angle))
def ang_torcional(n1):
    while True:
        n1 = input("Please put your list of angles: ")
        try:
            all(isinstance(item,int)for item in n1)
            result = Torcional(n1)
            recept_operations.append(result)
            return result
        except ValueError:
            print("One of the inputs on the list of angles wasn't an integer, please rewrite them carefully, remember not to write them with the °!")
            continue
def radians_to_sexa(n1):
    while True:
        n1 = input("Please put the number of radians: ")
        try:
            val = int(n1)
            result = (1*(180/pi))
            recept_operations.append(result)
            return result
        except ValueError:
            print("The input you gave is no an integer, please rewrite it carefully")
            continue
            
if election == "1":
    operations = operations_basics
    no_operation = input()
    if no_operation == "1":
        print(str("Your result is {0}").format(sum_bas(n1,n2)))
    elif no_operation == "2":
        print(str("Your result is {0}").format(subs_bas(n1,n2)))
        
