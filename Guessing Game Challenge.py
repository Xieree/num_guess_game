#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Guessing Game Challenge
# 
# Let's use `while` loops to create a guessing game.
# 
# The Challenge:
# 
# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
# 
# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 2. On a player's first turn, if their guess is
#  * within 10 of the number, return "WARM!"
#  * further than 10 away from the number, return "COLD!"
# 3. On all subsequent turns, if a guess is 
#  * closer to the number than the previous guess return "WARMER!"
#  * farther from the number than the previous guess, return "COLDER!"
# 4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!
# 
# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided. Good luck!
# 

# #### First, pick a random integer from 1 to 100 using the random module and assign it to a variable
# 
# Note: `random.randint(a,b)` returns a random integer in range `[a, b]`, including both end points.

# In[1]:


from random import randint
num = randint(1,100)


# #### Next, print an introduction to the game and explain the rules

# In[2]:


print("Welcome to the guessing game! Here you will try to guess the random number generated by the system.")
print("The number will be between 1 and 100, including both end values.")

print("You will keep guessing until you guess the random number correctly.")
print("When you guessed correctly, I will tell you along with the number of tries you took.\n")

print("If you are within 10 of the number, I will tell you WARM.")
print("If you are more than 10 from the number, I will tell you COLD.")

print("After your guess, if your next guess is closer to the number, I will tell you WARMER.")
print("If your next guess is further away, I will tell you COLDER.")


# #### Create a list to store guesses
# 
# Hint: zero is a good placeholder value. It's useful because it evaluates to "False"

# In[3]:


guess = []


# #### Write a `while` loop that asks for a valid guess. Test it a few times to make sure it works.

# In[4]:


while True:
    my_guess = int(input("What do you think is the number? "))
    if my_guess<1 or my_guess>100:
        print("The number you selected is out of bounds. Please choose a number within the range of 1 to 100.")
    else:
        print(f"Your guess is {my_guess}.")
        break
    pass


# #### Write a `while` loop that compares the player's guess to our number. If the player guesses correctly, break from the loop. Otherwise, tell the player if they're warmer or colder, and continue asking for guesses.
# 
# Some hints:
# * it may help to sketch out all possible combinations on paper first!
# * you can use the `abs()` function to find the positive difference between two numbers
# * if you append all new guesses to the list, then the previous guess is given as `guesses[-2]`

# In[5]:


while True:
    if my_guess==num:
        guess.append(my_guess)
        print(f"You guessed the number! It took {len(guess)} tries.")
        False
        break
        
    else:
        guess.append(my_guess)
        
        if abs(my_guess-num)<=10:
            print("Keep going, your guess is WARM.")
            
            if len(guess)>1:
                if (abs(num-guess[-2]))<(abs(num-guess[-1])):
                    print("You're getting COLDER.")
                    pass
                else:
                    print("You're getting WARMER.")
                    pass
        
        else:
            print("Keep going, your guess is COLD.")
            
            if len(guess)>1:
                if (abs(num-guess[-2]))<(abs(num-guess[-1])):
                    print("You're getting COLDER.")
                    pass
                else:
                    print("You're getting WARMER.")
                    pass
                
        my_guess = int(input("Try a different number. Your new guess is: "))
        if my_guess<1 or my_guess>100:
            print("The number you selected is out of bounds. Please choose a number within the range of 1 to 100.")
        else:
            pass
        
        True
        
    pass
    


# That's it! You've just programmed your first game!
# 
# In the next section we'll learn how to turn some of these repetitive actions into *functions* that can be called whenever we need them.

# ### Good Job!
