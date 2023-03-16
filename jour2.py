# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:11:29 2023

@author: aubru
"""

def My_print_hello():
    print ('Hello world')
    
#My_print_hello()

def My_print_name(name):
    print (name)
    
#My_print_name('Helio')

def Add(num1,num2):
    print(num1 + num2)
    
#Add(1,2)

def GetHello():
    print('Hello la Plateforme')
    
#GetHello()

def calcule(num1,op,num2):
    if op=='+':
        print(num1 + num2)
    elif op=='-':
        print(num1 - num2)
    elif op=='*':
        print(num1 * num2)
    elif op=='/':
        print(num1 / num2)
    elif op=='%':
        print(num1 % num2)
        
#calcule(5,'+',8)
#calcule(5,'-',8)
#calcule(5,'*',8)
#calcule(5,'/',8)
#calcule(5,'%',8)

def job6(nombre):
    if nombre<0:
        print('négatif')
    else:
        print('positif')
        
#job6(5)
#job6(-5)

def job7(langage):
    if langage=='javascript':
        print('tu es un developpeur web')
    elif langage=='python':
        print('tu es un developpeur IA')
    elif langage=='java':
        print('tu es un developpeur logiciel')
    elif langage=='reactjs':
        print('tu es un developpeur mobile')
    else:
        print('un jour, je serai le meilleur devoloppeur...')
        
#job7('javascript')
#job7('python')
#job7('java')
#job7('reactjs')
#job7('sacha de bourg palette')

def job8(type, saison ):
    if type=='fruits' and saison=='hiver':
        print('orange, mandarine et kiwi')
    if type=='fruits' and saison=='ete':
        print('poire, fraise, cassis')
    if type=='legume' and saison=='hiver':
        print('carotte, topinambour, endive ----> c pas bon')
    if type=='legume' and saison=='ete':
        print('artichaut, aubergine, navet')
        
#job8('fruits','hiver')
#job8('fruits','ete')
#job8('legume','hiver')
#job8('legume','ete')
        