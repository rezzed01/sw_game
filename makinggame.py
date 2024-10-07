import pyfiglet
import random

banner=pyfiglet.figlet_format("S , W , G")
print(banner)

''' 1 for snak
2 for water
3 for gun
'''
a =("S: \"SNAKE\"\n W: \"WATER\"\n G: \"GUN\"")
print(a)
computer = random.choice([1, 2, 3,])
yourstr = input("ENTER YOUR CHOICHE FROM S,W,G:")
yourdict = {"s": 1, "w": 2, "g": 3,}
reversedict ={1: "snake", 2: "water", 3: "gun"}

you = yourdict[yourstr]


print(f"YOU CHOOSE: {reversedict[you]}\nCOMPUTER CHOOSE: {reversedict[computer]}")

if(computer == you):
  print("ITS DRAW")

else:
  if(computer ==1 and you ==2):
    print("YOU LOSE")

  elif(computer ==2 and you ==3):
    print("YOU LOSE")

  elif(computer ==3 and you ==1):
    print("YOU LOSE")

  elif(computer ==2 and you ==1):
    print("YOU WIN")

  elif(computer ==3 and you ==2):
    print("YOU WIN")

  elif(computer ==1 and you ==3):
    print("YOU WIN")

  else:
    print("SOMETHING WENT WRGONES TO YOU")

