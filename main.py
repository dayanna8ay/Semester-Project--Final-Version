print("-----------------------------------------------------------")

print("                       Welcome to")
print(""" 
   ╔══╗──╔═╦╗────╔╦╗────────╔═╦╗──────╔═╗──╔╦╗───╔══╗
   ╚╗╗╠═╗╚╗║╠═╦╦╗║╔╬═╦╦═╦╦╦╗╚╗║╠═╦╦╦╦╗║╔╬═╦╝╠╬═╦╦╩╦╗║
   ╔╩╝║╬║╔╩╗║╬║║║║╚╣║║║╬║║║║╔╩╗║╬║║║╔╝║╚╣╬║╬║║║║║╬╠╔╝
   ╚══╩═╝╚══╩═╩═╝╚╩╩╩═╩═╩══╝╚══╩═╩═╩╝─╚═╩═╩═╩╩╩═╬╗╠╣
   ─────────────────────────────────────────────╚═╩╝
""")
print("In this game you will be tested on how well you know your coding. Pick from the two quizzes, and that is what you'll be tested on. At the end, your score will be given to you. So, have you truly learned? ")
print ("")
print ("When you're ready, type in 'START'")

answer=input()
while answer !="START":
  print ("....Well, do you want to play or not?   (Remember to type in all Caps!")
  answer = input("When you're ready, type in 'START'")
print("Let's go!☆～（ゝ。∂）")
ans=0
if (ans==0):
  print("-----------------------------------------------------------")
  print("                   Pick one of the 4:")
  print("1: Binary")
  print("2: Logic Multiple Choice")
  print("3: Total Points")
  print("4. Quit")
  print("Type the number in. (Ex: 1)")
  ans=int(input())


totalpoints=0 # This is used to keep track of total points
#ans=int(input())
while (ans !=4):
  if ans==1: #If the user choices option 1: Binary.
    x=3 # This is the amount of tries that the user has
    print("Which is the correct conversion from the binary (base-2) number 1011 to decimal (base-10)")
    print("9, 10, 16, 11")
    ansQ1=11
    userinput1=int(input())
    while(userinput1 != ansQ1):
      print("") # This is used for spacing purposes
      print("Incorrect answer. Try again.")
      print("You have " + str(x-1) + " tries left.")
      x=x-1
      userinput1=int(input())
      if userinput1 != ansQ1:
        if x==1:
          print("") # This is used for spacing purposes
          print("You have run out of tries. Next question.")
          print("") # This is for spacing purposes
          x=x-1
          userinput1=ansQ1
    
    if (userinput1 == ansQ1):
      if(x != 0):
        print("") # This is used for spacing purposes
        print("Correct! You got a point!")
        print("") # This is for spacing purposes
        totalpoints=totalpoints+1
  
  # Question 2 Now
    print("Write the correct conversion of the decimal (base-10) number 21 to binary (base-2).")
    print("10101, 10010, 11000, 00101")
    x=3
    ansQ1=10101
    userinput1=int(input())
    while(userinput1 != ansQ1):
      print("") # This is used for spacing purposes
      print("Incorrect answer. Try again.")
      print("You have " + str(x-1) + " tries left.")
      x=x-1
      userinput1=int(input())
      if userinput1 != ansQ1:
        if x==1:
          print("") # This is used for spacing purposes
          print("You have run out of tries. Next question.")
          print("") # This is for spacing purposes
          x=x-1
          userinput1=ansQ1
    
    if (userinput1 == ansQ1):
      if(x != 0):
        print("") # This is used for spacing purposes
        print("Correct! You got a point!")
        print("") # This is for spacing purposes
        totalpoints=totalpoints+1
  
  # Question #3
    print("Choose which of the following binary (base-2) numbers is the LARGEST?")
    print("111100, 001111, 110110, 101111")
    x=3
    ansQ1=111100
    userinput1=int(input())
    while(userinput1 != ansQ1):
      print("") # This is used for spacing purposes
      print("Incorrect answer. Try again.")
      print("You have " + str(x-1) + " tries left.")
      x=x-1
      userinput1=int(input())
      if userinput1 != ansQ1:
        if x==1:
          print("") # This is used for spacing purposes
          print("You have run out of tries. Next question.")
          print("") # This is for spacing purposes
          x=x-1
          userinput1=ansQ1
    
    if (userinput1 == ansQ1):
      if(x != 0):
        print("") # This is used for spacing purposes
        print("Correct! You got a point!")
        print("") # This is for spacing purposes
        totalpoints=totalpoints+1
  
    print("You are now done with this section! Look at the menu and decide")
    print("                   Pick one of the 4:")
    print("1: Binary")
    print("2: Logic Multiple Choice")
    print("3: Total Points")
    print("4: Quit")
    ans=int(input())
  

#---------------------------------------------------------

  if ans==2: #If the user choices option 2: Logic Multiple Choice.
    x=3 # This is the amount of tries that the user has
    print("") # Spacing purposes
    print('Which of the following will declare a variable "time" and set it equal to "six o clock?"')
    print("1. time=5")
    print('2. time="six o clock"')
    print('3. "time"=6')
    print('4. "time"="six o clock"')
    ansQ1=4
    userinput1=int(input())
    while(userinput1 != ansQ1):
      print("") # This is used for spacing purposes
      print("Incorrect answer. Try again.")
      print("You have " + str(x-1) + " tries left.")
      x=x-1
      userinput1=int(input())
      if userinput1 != ansQ1:
        if x==1:
          print("") # This is used for spacing purposes
          print("You have run out of tries. Next question.")
          print("") # This is for spacing purposes
          x=x-1
          userinput1=ansQ1
    
    if (userinput1 == ansQ1):
      if(x != 0):
        print("") # This is used for spacing purposes
        print("Correct! You got a point!")
        print("") # This is for spacing purposes
        totalpoints=totalpoints+1
  
  # Question 2 for part 2 Now
    print('Which of the following would create a variable named "cars" and sets it to the integer 4?')
    print('1. cars="4"')
    print('2. "cars"=4')
    print('3. cars="pollution"')
    print('4. cars=4')
    ansQ1=4
    x=3
    userinput1=int(input())
    while(userinput1 != ansQ1):
      print("") # This is used for spacing purposes
      print("Incorrect answer. Try again.")
      print("You have " + str(x-1) + " tries left.")
      x=x-1
      userinput1=int(input())
      if userinput1 != ansQ1:
        if x==1:
          print("") # This is used for spacing purposes
          print("You have run out of tries. Next question.")
          print("") # This is for spacing purposes
          x=x-1
          userinput1=ansQ1
    
    if (userinput1 == ansQ1):
      if(x != 0):
        print("") # This is used for spacing purposes
        print("Correct! You got a point!")
        print("") # This is for spacing purposes
        totalpoints=totalpoints+1
  
  # Question #3 for part 2
    print('Which of the following would declare a variable called textInteger and set it equal to the string "19"')
    print('1. "textInteger" = "19"')
    print('2. textInteger = 19')
    print('3. 19 = textInteger')
    print('4. textInteger = "19"')
    ansQ1=2
    x=3
    userinput1=int(input())
    while(userinput1 != ansQ1):
      print("") # This is used for spacing purposes
      print("Incorrect answer. Try again.")
      print("You have " + str(x-1) + " tries left.")
      x=x-1
      userinput1=int(input())
      if userinput1 != ansQ1:
        if x==1:
          print("") # This is used for spacing purposes
          print("You have run out of tries. Next question.")
          print("") # This is for spacing purposes
          x=x-1
          userinput1=ansQ1
    
    if (userinput1 == ansQ1):
      if(x != 0):
        print("") # This is used for spacing purposes
        print("Correct! You got a point!")
        print("") # This is for spacing purposes
        totalpoints=totalpoints+1
    print("You are now done with this section! Look at the menu and decide")
    print("                   Pick one of the 4:")
    print("1: Binary")
    print("2: Logic Multiple Choice")
    print("3: Total Points")
    print("4: Quit")
    ans=int(input())

#-------------------------------------------------------
  if ans==3: #If the user choices option 3: Total points.
    print("") # This is for spacing purposes
    print("Here are your total points: " + str(totalpoints))
    print("Great job!")
    print("You can get more points or quit")
    print("                   Pick one of the 4:")
    print("1: Binary")
    print("2: Logic Multiple Choice")
    print("3: Total Points")
    print("4. Quit")
    ans=int(input())

#---------------------------------------------------------
if ans==4: # This is for option 4: Quit
  print("") # This is for spacing purposes
  print("Have a good one!")


