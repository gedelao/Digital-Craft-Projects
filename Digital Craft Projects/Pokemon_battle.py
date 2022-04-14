print("""

  _ __   ___ | | _____ _ __ ___   ___  _ __  
 | '_ \ / _ \| |/ / _ \ '_ ` _ \ / _ \| '_ \ 
 | |_) | (_) |   <  __/ | | | | | (_) | | | |
 | .__/ \___/|_|\_\___|_| |_| |_|\___/|_| |_|
 |_|                                                         


""")




import random ##allows for random sequence to occur
import os
import sys ## allows for system input and output
import time ## allows for a pause between code

seconds =0.04
def run(str):
  for letter in str:
     sys.stdout.write(letter)
     sys.stdout.flush() 
     time.sleep(seconds)
  print()

def slow_inp(str):
  for letter in str:
     sys.stdout.write(letter)
     sys.stdout.flush()
     time.sleep(seconds)
  input()

Gengar_health = 60
Charizard_health = 60
Health = 70
Health < 70
Attack = 90
Speed= 100

types= ['Fighting','Rock','Ice','Dragon','Fairy','Bug','Ghost','Steel','Water','Grass','Dark']
moves = ['Dragon Claw','Flamethrower','Ice Beam','Thunder Bolt']
opponent = ['Gengar', 'Charizard']
Gengar = ['Shadow Ball ','Bite','Shadow Punch','Confusion']
Charizard = ['Fire Blast','Fly','Fire Punch','Sunny Day']
names = ['Blake','Ash', 'Cynthia', 'Gary',' Brock',' Misty',' Tracy',' Cynthia']
Charizard= random.choice(Charizard)
Gengar= random.choice(Gengar)
opponent=random.choice(opponent)
names= random.choice(names)
types=random.choice(types)


pokemon_journey = input('Welcome to the world of pokemon! Would you like to be the best like no one ever was? Yes/No ')
if pokemon_journey == "Yes":
  os.system('clear')
  run("The Kanto region is inhabited with an array of pokemons who live among humans. Before begining your journery, tell us about yourself. ")
if pokemon_journey =="No":
  input("It was all a dream")
  os.system('clear')
  exit()
trainer = input("What is your name? ")
gender = input("Are you Male or Female? ")
if gender == "Male":
    os.system('clear')
if gender == "Female":
    os.system('clear')
id = print("Trainer, "+ trainer + ":")
run("It is time to embark on your journey! ")
input("Press Enter: ")

while True:
  os.system('clear')
  if Health < 1 :
    run("You have lost! ")
    run("Don't give up! Try again. ")
    break
  if Charizard_health < 1:
    run("Congrats, you won!! ")
    break
  if Gengar_health < 1:
    run("you have won the battle!")
    break
  print(f'''Halt...
    You have been approached by trainer, {names}
    {names} wants to battle!
    {names} used {opponent}
    ''')
  print('''
  

  ''')
  run("Dragonite's health is: "+ str(Health))
  run("[1] attack")
  run("[2] enemy Stats")
  run("[3] Forfeit match")
  run("What do you want to do? ")
  option=input("")
  if option == "3":
     run("You have forfeited the battle")
     break
  if option == "2":
    os.system('clear')
    if option == "Charizard":
      run(names + " Charizard health is:")
      print(Charizard_health)
      print("90 Attack")
      print("70 Speed")
      input("Press Enter")
    if opponent == "Gengar":
      run(names + " Gengar health is:")
      print( Gengar_health) 
      print("Health points")
      print("55 Attack")
      print("70 Speed")
    input("Press Enter: ")
  if option == "1":
    os.system('clear')
    run(" [1] Dragon Claw")
    run(" [2] Flamethrower")
    run(" [3] Ice Beam")
    run(" [4] Thunder Bolt")
    fight =input("Which Attack will you Dragonite use? ")
    if opponent == "Charizard" and  fight == "4":
      Charizard_health -= 40
      run("It's Super Effective! Charizard lost 40 HP ")
    if opponent== "Charizard" and fight =="3":
      Charizard_health -= 25
      run(" Charizard lost 25 HP")
    if opponent == "Charizard" and fight == "2":
      run("It's not effective on Charizard ")
      Health -= 1
    if opponent == "Charizard" and fight == "1":
      Charizard_health -= 10
      run("Charizard lost 10 HP")
    if opponent == "Gengar" and fight =="1":
      Gengar_health -=10
      run("Gengar lost 10 HP")
    if opponent == "Gengar" and fight =="2":
      run("Gengar los 10 HP")
      Gengar_health -= 10
    if opponent == "Gengar" and fight =="3":
      Gengar_health -=40
      run("Gengar lost 40 HP")
    if opponent == "Gengar" and fight =="4":
      Gengar_health -= 25
      run("Gengar lost 25 HP")
    print('''
    
    
    
    ''')
    if Charizard_health < 1:
      run("Congrats, you have won!!")
      break
    if Gengar_health < 1:
      run("Congrats, you have won!!")
      break
    if opponent == "Charizard":
      run(names + "  Charizard used " + Charizard)
      if Charizard == "Fire Blast":
         Health -= 35
         run("Dragonite lost 35 HP")
      if Charizard== "Fly":
         Health -= 40
         run("Dragonite lost 40 HP")
      if Charizard == "Fire Punch":
         Health -=20
         run("Dragonite lost 20 HP")
      if Charizard == "Sunny Day":
         run("Fire's attack strengthend ")
    if opponent == "Gengar":
      run(names + " Gengar used "+ Gengar)
      if Gengar == "Bite":
         Health -= 35
         run("Dragonite lost 35 HP")
      if Gengar =="Shadow Punch":
         Health -= 10
         run("Dragonite lost 10 HP")
      if Gengar =="Confusion":
         Health -=50
         run("Dragonite lost 50 HP")
      if Gengar =="Shadow Ball":
         Health -=50
         run("Dragonite lost 50 HP")
      input("Press Enter: ")

