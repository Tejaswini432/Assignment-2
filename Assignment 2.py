# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:35:47 2020

@author: Tejaswini...!
"""
#to check whether two numbers are equal or not
a=float(input("enter the value of a:"))
b=float(input("enter the value of b:"))
if (a == b):
    print("a is equal to b")
if ( a != b):
    print("a is not equal to b")    
    
#to check whether the given 3 inputs are:
#1.equal
a=float(input("enter the value of a:"))
b=float(input("enter the value of b:"))
c=float(input("enter the value of c:"))
if (a == b == c):
   print("the given 3 inputs are equal")    
else:
    print("the given 3 inputs are not equal")

#2.any of two are equal
a=float(input("enter the value of a:"))
b=float(input("enter the value of b:")) 
c=float(input("enter the value of c:"))
if (a == b != c):
    print("a and b are equal")
if(a != b == c):
    print("b and c are equal")
if(a == c != b):
    print("a and c are equal") 
elif(a != b != c):
    print("none are equal")    
    
#to check whether the sum of two numbers is:
#1.greater than 5    
#2.smaller than 5
#3.equal to 5    
a=float(input("enter the value of a:"))
b=float(input("enter the value of b:"))
c=a+b;
if (c > 5):
   print("c is greater than 5")
if (c < 5):
   print(" c is smaller than 5") 
elif (c == 5):
    print("c is equal to 5")   
    
#to check whether the input is graeter than passing mark or not
a=float(input("enter the value of a:"))
if ( a > 35 ):
   print("the marks are greater than the passing mark")
if ( a == 35):
   print("the mark is equal to passing mark")
elif ( a < 35):
   print("the marks are less than passing mark")
   
#to find the max of three numbers
a=float(input("enter the value of a:"))
b=float(input("enter the value of b:"))
c=float(input("enter the value of c:"))
if ( a > b ) and ( a > c ):
    print(" a is the largest ")
if ( b > a ) and ( b > c ):
    print(" b is the largest ")
if ( c > a ) and ( c > b ):
    print(" c is the largest ")    
else:
    print("none")
     