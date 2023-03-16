# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:30:39 2023

@author: aubru
"""

def job1 ():
    print (10 + 3)
    print (10 - 3)
    print (10 * 3)
    print (10 / 3)
    print (10 % 3)
    print (10 // 3)

#job1()

def job2():
    print (10 + 3)

#job2()

def job4():
    print('abcdefghijklmnopqrstuvwxyz')
    
#job4()

def job5():
    print('zyxwvutsrpqonmlkjihgfedcba')
    
#job5()

def job6():
    ma_string='Je suis un STRING'
    print(ma_string)
    
#job6()

def job7(num1,num2):
    print(num1 + num2)
    
#job7(40, 2)

def job8(num1,num2):
    print(num1 * num2)
    
#job8(3,14)

def job9(chaine):
    e=False
    for i in range(len(chaine)):
        if chaine[i]=='e':
            e=True
    if e:
        print('contient e')
    else:
        print('ne contient pas e')
        
#job9('ecole')
#job9('non')