choice1 = " "
choice2 = " "
choice3 = " "

#Choice 1
choice1 = input("It is the finals for your math class, and you need to pass. You can tell that " \
"you are not doing well. Do you CHEAT or SUFFER? ")

#Choice 2
if choice1.lower() == "cheat" : choice2 = input("You manage to pass the finals, but barely. There is now a sinking feeling in your stomach, and guilt sets in. Do you tell the TRUTH, or keep up the LIE? ")
elif choice1.lower() == "suffer" : choice2 = input("Unfortunately, your lack of studying was relfected in the grade of the test, and you failed. Do you TELL your parents, or keep QUIET? ")
else: print("That was not an option. Please reset the game to try again.")

#Choice 3
#Cheat Path
if choice2.lower() == "truth" and choice1.lower() == "cheat": choice3 = input("Work in progress 1 ")
elif choice2.lower() == "lie" and choice1.lower() == "cheat": choice3 = input("Work in progress 2 ")

#Suffer Path
elif choice2.lower() == "tell" and choice1.lower() == "suffer": choice3 = input("Work in progress 3 ")
elif choice2.lower() == "quiet" and choice1.lower() == "suffer": choice3 = input("work in progress 4 ")
else: print("You have inputted an invalid option. Please try again")

#Result
#Truth Path
if choice3.lower() == "cheese" and choice2.lower() == "truth": print("hi")
elif choice3.lower() == "bacon" and choice2.lower() == "truth": print("hi")
elif choice3.lower() == "ham" and choice2.lower() == "truth": print("hi")

#Lie Path
elif choice3.lower() == "filler" and choice2.lower() == "lie": print("hi")
elif choice3.lower() == "filler1" and choice2.lower() == "lie": print("hi")

#Tell Path
elif choice3.lower() == "filler2" and choice2.lower() == "tell": print("hi")
elif choice3.lower() == "filler4" and choice2.lower() == "tell": print("hi")

#Quiet Path
elif choice3.lower() == "filler5" and choice2.lower() == "quiet": print("hi")
elif choice3.lower() == "filler6" and choice2.lower() == "quiet": print("hi")
else: print("My deepest apologies, but you have selected a choice that is not valid. Please try the game again.")
