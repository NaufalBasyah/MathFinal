# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 02:42:43 2019

@author: Naufal Basyah
"""
import pygame
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from Settings import *

setting=Settings()                                                  #intializing the background and setting objects
bg=BackGround("Screen.jpg",setting)
textlist=[]
textinput=[]
textlistwords=[]                                                     #containers to store words and lines of words
textinputwords=[]
count=0

def inputBox(*count):
    text= newTextBox("Enter text here",setting.screenWidth*.05+25,setting.screenHeight/2-10,setting.screenWidth*.43,0,0,35)
    showTextBox(text)                                                                                                      #a method to create a text input box that will store the words type in it in a list
    entry=textBoxInput(text)
    textinput.append(entry)
    return entry
            
    
    
def runKeyboardWarrior():
    global textinput
    global textinputwords
    global count
    global g
    global n
    global difApprox
    global x
    count=0
    pygame.init()
    pygame.font.init()
    screen=screenSize(setting.screenWidth,setting.screenHeight)
    myFont = pygame.font.SysFont("Courier",30,True)                                                 #font setting for the instruction text and printed paragraph from the text file
    myFont2 = pygame.font.SysFont("Courier",35,True)
    theClock = pygame.time.Clock()
    Fps=10                                                                                     #setting the Fps
    run=True
    

    theClock.tick(Fps)
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:                                                         #x icon to quit the window and game
                run=False
        if count%3==0 and count!=0:
            screen.blit(bg.bg_image,(0,0))
            instruction1=myFont2.render("ENTER AN X VALUE TO COMPUTE THE APPROXIMATION",False,(120,120,120))
            instruction2=myFont2.render("FOLLOWED BY AN ENTER TO SUBMIT.",False,(120,120,120))                         #blitting the background and instruction text
            screen.blit(instruction1,(setting.screenWidth*.10,setting.screenHeight/2-150))
            screen.blit(instruction2,(setting.screenWidth*.10,setting.screenHeight/2-115))
            x=inputBox(count)
        elif count%2==0 and count!=0:
            screen.blit(bg.bg_image,(0,0))
            instruction1=myFont2.render("ENTER NUMBER OF ITERATION FOR THE APPROXIMATION VALUE",False,(120,120,120))
            instruction2=myFont2.render("FOLLOWED BY AN ENTER TO SUBMIT.",False,(120,120,120))                         #blitting the background and instruction text
            screen.blit(instruction1,(setting.screenWidth*.10,setting.screenHeight/2-150))
            screen.blit(instruction2,(setting.screenWidth*.10,setting.screenHeight/2-115))
            n=inputBox(count)
        else:
            screen.blit(bg.bg_image,(0,0))
            instruction1=myFont2.render("ENTER THE EQUATION TO DIFFERENTIATE,",False,(120,120,120))
            instruction2=myFont2.render("FOLLOWED BY AN ENTER TO SUBMIT.",False,(120,120,120))                         #blitting the background and instruction text
            screen.blit(instruction1,(setting.screenWidth*.10,setting.screenHeight/2-150))
            screen.blit(instruction2,(setting.screenWidth*.10,setting.screenHeight/2-115))
            
            equation=inputBox(count)                                                  #creating the input box
            g= lambda x: eval(equation)
            
        
    return 0



runKeyboardWarrior()
