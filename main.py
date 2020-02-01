from random import randint
global health
global enemyHealth
global enemyDmgUp
global enemyGraze
global enemyHit
global bossHealth
health = 20
enemyHealth = 10 
bossHealth = 30
enemyGraze = enemyHealth - 3
enemyHit = enemyHealth - 5
print(".%%%%%%..%%..%%..%%%%%%.")
print("...%%....%%..%%..%%.....")
print("...%%....%%%%%%..%%%%...")
print("...%%....%%..%%..%%.....")
print("...%%....%%..%%..%%%%%%.")
print("........................")
print(".%%%%%....%%%%...%%%%%...%%..%%.")
print(".%%..%%..%%..%%..%%..%%..%%.%%..")
print(".%%..%%..%%%%%%..%%%%%...%%%%...")
print(".%%..%%..%%..%%..%%..%%..%%.%%..")
print(".%%%%%...%%..%%..%%..%%..%%..%%.")
print("................................") 
print(".%%%%%%...%%%%...%%...%%..%%%%%%..%%%%%..")
print("...%%....%%..%%..%%...%%..%%......%%..%%.")
print("...%%....%%..%%..%%.%.%%..%%%%....%%%%%..")
print("...%%....%%..%%..%%%%%%%..%%......%%..%%.")
print("...%%.....%%%%....%%.%%...%%%%%%..%%..%%.")
print(".........................................")
print("made by Cameron Spurvey and Hunter Lafleur")
print(".........................................")
print("Press enter to progress")
#game intro
input()
print("You are a lone gunslinger trying to defeat your enemy.")
input()
print("The Man In Black.")
input()
print("He is at the top of the dark tower, trying to destroy it to get to another earth to do the bad things he did to yours.")
input()
print("You are at the bottom of the tower, you must get to the top to defeat him.")
print("But there are bad guys through out the whole tower.")
input()
print('You must choose your path to the top, some ways are quicker then others, but choose wisely for there is danger.')
#rules
def combatr():
  print("Combat rules")
  print("1. Combat is turn based.")
  print()
  print('2. if you choose to fight you will be presented with different moves some stronger then others that will require a higher roll to land. you will enter 1/2/3/4 to use one of the moves.')
  print("3.to make decisions there are two 5 sided dice")


def expor():
  print("exploration rules")
  print('you will be presented with multipule options for your direction wiht a breif description of the path ahead, you will then have to enter one of the directions (up/down/north/south/west/east)')
  print("to make decisions there are two 5 sided dice")

def rulebook():
  print("would you like to see combat rules or exploration rules?")
  coorex = input()
  if coorex == "combat":
    print()
    combatr()
  else:
    print()
    expor()
  print()
  print("would you like to read the rules again?")
  yorn = input()
  if yorn == "yes":
    print()
    rulebook()

print()
print("Would you like to see the rules?")
ruleinn = input()
if ruleinn == "yes":
  print()
  print("would you like to see combat rules or exploration rules?")
  coorexx = input()
  if coorexx == "combat":
    print()
    combatr()
  else:
    print()
    expor()
  print()
  print("would you like to read the rules again?")
  yornn = input()
  if yornn == "yes":
    print()
    rulebook()  
#game start
print()
enter = input("You are at the bottom of the tower facing north towards the enterance, which way would you like to go? (north, south) ")
if enter == "north":
  print()
  print(' You enter the tower and begin your journey.')
  print()
if enter == "south":
    print()
    print("you decide not to enter and vanish into the fog.")
    print()
    print("end")
    exit()
if enter == "bad":
  print()
  print("You place c4 on the side of the tower.")
  print()
  
  print("you walk away from the tower and shoot the c4")
  print()
  print("Game Over")
  print()
  print("congrats! you found the secret ending!")
  print()
  exit()

##entering the tower, aka floor1##

print('you look around the room, there seems to be two broken staircases leading to doors on the east and west sides of the tower. there is a ledge you can use to get to them')
print()
print('There is also a door in the middle that you would have to jump to from the ledge, you might be able to make the jump.')

def map1():
  print()
  print("What would you like to do? (North, East, West)")
  directt = input()
  if directt == "east":
    print()
    print("You go to the broken staircase to the east. There is nothing interesting here")
    print()
    map1()
  if directt == "west":
    print("You go to the broken staircase to the west. There is nothing interesting here")
    print()
    map1()
  if directt == "north":
    print("you head to the ledge infront of you. you are now ontop of the ledge.")
    
##floor 2 right door##

def rightDoor1():
  print("You are faced by an enemy!")
  input()
  print("Battle begin!")
  input()
  print("Your health:" + str(health))
  print("Enemy health:" + str(enemyHealth))
  print()
  print("the enemy spits in your eye")
  print()
  print("You shoot at the enemy")
  input()
  combat1()

##win condition for the first battle##

def bat1win():
  print("")
  print("you look around at the room and notice a weak wall to your left, you might be able to break it")
  print("")
  direct = input("left,back")
  global health
  if direct == ("left"):
    print("rolling...")
    roll = randint(2,10)
    if roll <= 4:
      print("you hit the wall and a brick hits your shoulder. -5 health")
      print()
      print(health)
      print()
      if health < 0:
        print("you died, game over")
        return
      else:
        bat1win()
    else:
      print("you hit the wall and it collapses")
      print()
      leftDoor()
  else:
    ledge()

##combat block##

def combat1():
  global health
  global enemyHealth
  enemyHealth == 10
  dmgRoll3 = randint(2,10)
  if dmgRoll3 < 4:
    print("you missed")
    input()
    enemyCombat()
  elif dmgRoll3 > 4 < 7:
    print("You grazed the enemy with your bullet!")
    enemyHealth -= 3
    print("enemy health: " + str(enemyHealth))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      bat1win()
      enemyHealth == 10
    elif health <= 0:
      print("Game over") 
      exit()
      enemyHealth == 10
      health == 20
    enemyCombat()
  else:
    print("you hit the enemy with you bullet!")
    enemyHealth -= 5
    print("enemy health: " + str(enemyHealth))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      bat1win()
      enemyHealth == 10
    elif health <= 0:
      print("Game over") 
      exit()
      enemyHealth == 10
      health == 20
    enemyCombat()  

def enemyCombat():
  global health
  global enemyHealth
  dmgRoll2 = randint(2,10)
  if dmgRoll2 < 4:
    print("The enemy missed")
    input()
    combat1()
  elif dmgRoll2 > 4 < 7:
    print("The enemy barely hit You!")
    health -= 3
    print("Health: " + str(health))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      bat1win()
    elif health <= 0:
      print("Game over") 
      exit()
      enemyHealth == 10
      health == 20
    combat1()
  else:
    print("The enemy hit You!")
    health -= 5
    print("Health: " + str(health))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      bat1win()
      enemyHealth == 10
    elif health <= 0:
      print("Game over") 
      exit()
      enemyHealth == 10
      health == 20
    combat1()

def combat2():
  global health
  global enemyHealth
  
  dmgRoll3 = randint(2,10)
  if dmgRoll3 < 4:
    print("you missed")
    input()
    enemyCombat1()
  elif dmgRoll3 > 4 < 7:
    print("You grazed the enemy with your bullet!")
    enemyHealth -= 3
    print("enemy health: " + str(enemyHealth))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      return
    elif health <= 0:
      print("Game over") 
      exit()
    enemyCombat1()
  else:
    print("you hit the enemy with you bullet!")
    enemyHealth -= 5
    print("enemy health: " + str(enemyHealth))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      return
    elif health <= 0:
      print("Game over") 
      exit() 
    enemyCombat1()  
  

def enemyCombat1():
  global health
  global enemyHealth
  dmgRoll2 = randint(2,10)
  if dmgRoll2 < 4:
    print("The enemy missed")
    input()
    combat2()
  elif dmgRoll2 > 4 < 7:
    print("The enemy barely hit You!")
    health -= 3
    print("Health: " + str(health))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      return
      enemyHealth =+ 10
    elif health <= 0:
      print("Game over") 
      exit()
      enemyHealth =+ 10
    combat2()
  else:
    print("The enemy hit You!")
    health -= 5
    print("Health: " + str(health))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      return
    elif health <= 0:
      print("Game over") 
      exit()
      enemyHealth =+ 10
    combat2()

def combat3():
  global health
  global enemyHealth
  enemyHealth == 10
  dmgRoll3 = randint(2,10)
  if dmgRoll3 < 4:
    print("you missed")
    input()
    enemyCombat2()
  elif dmgRoll3 > 4 < 7:
    print("You grazed the enemy with your bullet!")
    enemyHealth -= 3
    print("enemy health: " + str(enemyHealth))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      floor3PostCombat()
      enemyHealth =+ 10
    elif health <= 0:
      print("Game over") 
      exit()
      enemyHealth =+ 10
    enemyCombat2()
  else:
    print("you hit the enemy with you bullet!")
    enemyHealth -= 5
    print("enemy health: " + str(enemyHealth))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      floor3PostCombat()
      enemyHealth =+ 10
    elif health <= 0:
      print("Game over") 
      exit() 
      enemyHealth =+ 10
    enemyCombat2()  
  

def enemyCombat2():
  global health
  global enemyHealth
  dmgRoll2 = randint(2,10)
  if dmgRoll2 < 4:
    print("The enemy missed")
    input()
    combat3()
  elif dmgRoll2 > 4 < 7:
    print("The enemy barely hit You!")
    health -= 3
    print("Health: " + str(health))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      floor3PostCombat()
    elif health <= 0:
      print("Game over") 
      exit()
    combat3()
  else:
    print("The enemy hit You!")
    health -= 5
    print("Health: " + str(health))
    input()
    if enemyHealth <= 0:
      print("YOU WIN")
      floor3PostCombat()
    elif health <= 0:
      print("Game over") 
      exit()
    combat3()    

##sneaky enterence to the 3rd floor##

def floor3sneak():
  print("The path ends at grate, there seems to be someone in the room.")
  print('you quietly break the grate free and jump to the floor.')
  print('It is an enemy!!')
  combat3()
  floor3PostCombat()

##entering 4th floor##

def floor4Enter():
  print('You go up the ladder and enter the 4th floor.')
  print('There is are barrels around the room in every direction.')
  floor4()

##floor4##

def floor4():
  global health
  print("There is a big heavy looking door to the north,barrels to the east and west and you look up and see a loft but you can't see if there is anything up there.")
  direc = input()
  if direc == "north":
    print("you head to the big door, it is heavy. would you like to open it?")
    bossDoor = input()
    if bossDoor == "yes":
      bossRoom()
    else:
      floor4()
  elif direc == "east":
    print("you head over to the barrels, they are open. someone already got to these.")
    floor4() 
  elif direc == "west":
    print("you head over to the barrels, they are open. There is a health pack inside! +10 health")
    health += 10
    print("health: " + str(health))
    floor4() 
  else:
    print("you head up the ladder into the loft, there is a crate. would you like to open it?")
    crate = input()
    if crate == "yes":
      rollGun = randint(2,10)
      if rollGun >= 8:
        print("you find a second gun inside the crate!")
        print("your damage is now doubled")
        print()
        print("you climb back down the ladder and head to the heavy door. you enter the room")
        bossRoomDoubleGun()
      else:
        print("there is nothing in the crate.")
        print("You climb back down the ladder.")
        floor4() 

##Boss fight##

def bossWin():
  print("My plans will continue on after me.")
  print('So do what you will, these things are bigger then you or me.')
  print('We mean nothing, you fight for nothing, you are nothing.')
  print("game over.")
  exit("thanks for playing")

def bossLose():
  print('Pathetic...')
  input()
  print('I expected more out of you.')
  print('Oh well I have other things to, you are just a minor inconvenence.')
  print('To see you fail not once, but twice, your father would be very dissapointed.')
  print('Enjoy the show.')
  print('As the world goes blank in a white flash, so do you.')
  exit()

def bossRoomDoubleGun():
  global health
  global bossHealth
  dmgRoll3 = randint(2,10)
  if dmgRoll3 < 4:
    print("you missed")
    input()
    bossCombat()
  elif dmgRoll3 > 4 < 7:
    print("You grazed the enemy with your bullet!")
    bossHealth -= 6
    print("Boss health: " + str(bossHealth))
    input()
    if bossHealth <= 0:
      print("YOU WIN")
      bossWin()
      bossHealth =+ 30
    elif health <= 0:
      print("Game over") 
      bossLose()
      bossHealth =+ 30
    bossCombat()
  else:
    print("you hit the enemy with you bullet!")
    bossHealth -= 10
    print("Boss health: " + str(bossHealth))
    input()
    if bossHealth <= 0:
      print("YOU WIN")
      bossWin()
      bossHealth =+ 30
    elif health <= 0:
      print("Game over") 
      bossLose() 
      bossHealth =+ 30
    bossCombat() 
def bossCombat():  
  global health
  global bossHealth
  dmgRoll2 = randint(2,10)
  if dmgRoll2 < 4:
    print("The enemy missed")
    input()
    bossRoomDoubleGun()
  elif dmgRoll2 > 4 < 7:
    print("The enemy barely hit You!")
    health -= 3
    print("Health: " + str(health))
    input()
    if bossHealth <= 0:
      print("YOU WIN")
      bossWin()
    elif health <= 0:
      print("Game over") 
      bossLose()
    bossRoomDoubleGun()
  else:
    print("The enemy hit You!")
    health -= 5
    print("Health: " + str(health))
    input()
    if bossHealth <= 0:
      print("YOU WIN")
      bossWin()
    elif health <= 0:
      print("Game over") 
      bossLose()
    bossRoomDoubleGun()    
  
def bossRoom():
  global bossHealth
  bossHealth = 30
  global health
  dmgRoll3 = randint(2,10)
  if dmgRoll3 < 4:
    print("you missed")
    input()
    bossCombat2()
  elif dmgRoll3 > 4 < 7:
    print("You grazed the enemy with your bullet!")
    bossHealth -= 3
    print("enemy health: " + str(bossHealth))
    input()
    if bossHealth <= 0:
      print("YOU WIN")
      bossWin()
      bossHealth =+ 30
    elif health <= 0:
      print("Game over") 
      bossLose()
      bossHealth =+ 30
    bossCombat2()
  else:
    print("you hit the enemy with you bullet!")
    bossHealth -= 5
    print("enemy health: " + str(enemyHealth))
    input()
    if bossHealth <= 0:
      print("YOU WIN")
      bossWin()
      bossHealth =+ 30
    elif health <= 0:
      print("Game over") 
      bossLose()
      bossHealth =+ 30
    bossCombat2()  
  

def bossCombat2():
  global health
  global bossHealth
  dmgRoll2 = randint(2,10)
  if dmgRoll2 < 4:
    print("The enemy missed")
    input()
    bossRoom()
  elif dmgRoll2 > 4 < 7:
    print("The enemy barely hit You!")
    health -= 3
    print("Health: " + str(health))
    input()
    if bossHealth <= 0:
      print("YOU WIN")
      floor3PostCombat()
    elif health <= 0:
      print("Game over") 
      exit()
    bossRoom()
  else:
    print("The enemy hit You!")
    health -= 5
    print("Health: " + str(health))
    input()
    if bossHealth <= 0:
      print("YOU WIN")
      floor3PostCombat()
    elif health <= 0:
      print("Game over") 
      exit()
    bossRoom()   
  

##entering floor 3##

def floor3Main():
  global health
  print('You enter the third floor.')
  print('ther is an enemy!!')
  combat3()
  print("you look around the room and notice some barrels to your left, there is also a door straight ahead of you.")
  floor3PostCombat()

##Floor3 Post Combat##

def floor3PostCombat():  
  global health
  print("you look around the room and notice some barrels to your left, there is also a door straight ahead of you.")
  print("north,west")
  direc = input()
  if direc == "north":
    print("you head to the door, its locked.")
    print("would you like to try and break it down, or pick the lock?")
    print()
    print("break,lockpick")
    borl = input()
    if borl == "break":
      roll = randint(2,10)
      if roll >= 5:
        print("you broke the door down")
        floor4Enter()
      else:
        print("you broke your arm trying to break the door down, -3 health")
        health -= 3
        print(health)
        floor3PostCombat()
    elif borl == "lockpick":
      roll2 = randint(2,10)
      if roll2 >= 6:
        print("you picked the lock and opened the door.")
        floor4Enter()
      else:
        print("you broke your lockpick.")
        floor3PostCombat()
  elif direc == "west":
    print("you walk over to the barrels, they look stong")
    print("open,shoot")
    brlinp = input()
    if brlinp == "open":
      print("you try to open the barrel, but you cant.")
      floor3PostCombat()
    elif brlinp == "shoot":
      print("you shoot the barrel and find a health kit inside! +7 health")
      health += 7
      print("health: " + str(health))
      floor3PostCombat()
      
##Floor 2 left door##

def leftDoor():
  print("You enter the room")
  
  print('It appears to be a storage room.')
  print()
  print('To the right there is a wall that looks weak, you might be able to break through it.')
  print()
  print('To the left of the room there are 5 barrels.')
  print()
  print('to the north of the room there is a stair case to the next level.')
  dr2 = input('which way would you like to go?')
  if dr2 == "left":
    print('You hed towards the barrels.')
    barrl = input('what would you like do?')
    print("break, open")
    if barrl == "open":
      print('You can not open the barrel.')
      leftDoor()
    elif barrl == "break":
      print("you shoot all the barrels and conviently fall apart, there seems to be somethings in the barrels.")
      clue = input("would you like to inspect the items?")
      if clue == "yes":
        return
      else:
        leftDoor()
  elif dr2 == "right":
    print('You head to the weak wall.')
    wall = input('The wall seems weak would you like to try to break through it?')
    if wall == "yes":
      roll2 = randint(2,10)
      if roll2 > 3:
        print("you break through the wall")
        rightDoor1()
      else:
        print("you hit the wall and a brick hits your shoulder. -5 health")
      print()
      print(health)
      print()
      if health < 0:
        print("you died, game over")
        exit()
    else:
      leftDoor()  
  elif dr2 == "north":
    print("You head to the staircase.")
    stir = input('Would you like to go up the stairs?')
    if stir == "yes":
      print('You go up the stairs.')
      floor3Main()
    else:
      leftDoor()

##Floor1.5##

map1()
print()
def ledge():
  print("What would you like to do? (up,left,right)")
  dir = input()
  if dir == "up":
    print()
    print("rolling....")
    input()
    roll = randint(2,10)
    if roll >= 6:
      print()
      print("you climb over the rail and are infront of the middle door.")
      print()
      print("would you like to go through the door?")
      dm1 = input()
      if dm1 == "yes":
        print("you go through the door in the middle")
        print("Its a path straight to the third floor.")
        floor3sneak()
    else: 
      print()
      print("critical fail! you fall and break your neck. you are dead.")
      print()
      print("game over")
      exit()
  if dir == "left":
    print()
    dl1 = input("you are now infront of the left door, would you like to go in?")
    if dl1 == "yes":
      print('You go through the door on the left.')
      leftDoor()
    else:
      ledge()
  if dir == "right":
    print()
    dr1 = input("you are now infront of the right door, would you like to go in?")
    if dr1 == "yes":
      print('You go through the door on the right.')
      rightDoor1()
  else:
    print()
    print("you climb back down to the ledge")
    ledge()
ledge()
floor3Main()




















