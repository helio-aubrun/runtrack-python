# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:21:44 2023

@author: aubru
"""

def job1 ():
    for i in range (21):
        print (i)
        
#job1()


def job2():
    for i in range (0,21,2):
        print (i)
        
#job2()

def job3 ():
    for i in range (101):
        if i!= 26:
            if i!= 37:
                if i!=88:
                    print (i)
                    
#job3()

def job4():
    for i in range (1,101):
        if i%3==0:
            if i%5==0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print (i)
        
#job4()

def job5():
    for n in range (1,1001):
        premier=True
        i=2
        while n>i and premier==True :
            if n%i==0 :
                premier=False
            i=i+1
        if premier:
            print(n)
        
#job5()

def job6():
    alpha='abcdefghijklmnopqrstuvwxyz'*10
    for i in range(len(alpha)):
        if i<len(alpha)-i:
            for i in range(i+1):
                print(alpha[:i], end='')
        print('\n')
        
#job6()

def job7(chaine):
    result = ''
    for caractere in chaine:
       result = caractere+result 
    print (result)
    
#job7('test')