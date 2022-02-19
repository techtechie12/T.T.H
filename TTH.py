from modulefinder import Module
import os
import pywhatkit as p
from pywhatkit.handwriting import text_to_handwriting
import wikipedia as wk
import pyfiglet
from colorama import Fore, Back, Style

while True:

  print(Fore.RED+ '''
                                  introducing TTH

This script is for special student, you will be able to convert text to handwriting.
this script for an educational purpose!!!!!
  ''') 

  input(Fore.WHITE+'Please enter key to start')
  os.system("clear")
  os.system("cls")
  
  a=pyfiglet.figlet_format("T . T . H")
  print(a)

  apr = input(Fore.GREEN+'[#]' " Please enter the info to handwriting for convert : ")
  try:
   rr=wk.summary(apr)
  except:
    print("not found")
    break
  print()
  print()
  app = input('''
 Example : writing.png
[#] Please enter the name of this file : ''')
     
  print()
  print()
  rgb = input('''
  1-green
  2-blue
[#] Enter the color name to change text color : ''')
  os.system("cls")
  os.system("clear")
  print()
  
  if rgb=="blue":
         print("Please wait...")
         print(p.text_to_handwriting(rr,app,[0, 0, 138]))
         os.system("cls")
         os.system("clear")
         print("-"*50)
         print("      ----complete----") 
         print("----PLease check the file----")
         print("-"*50)
  elif rgb=="green":
         print("Please wait...")
         print(p.text_to_handwriting(rr,app,[0, 128, 0]))
         os.system("cls")
         os.system("clear")
         print("-"*50)
         print("      ----complete----") 
         print("----PLease check the file----")
         print("-"*50)         
  else:
    print( Fore.RED+"[!] please correct the color name in the below")
    ww = input(Fore.LIGHTRED_EX+"Restart for press 'r' and quit to 'q' ")
    if ww=="r":
     print()
    elif ww=="q":
        print( Fore.GREEN+"-"*50)
        print( Fore.GREEN+"thanks for visiting")
        print( Fore.GREEN+"-"*50)
  break

  
