#!/usr/bin/env python
# coding: utf-8

# **Day 4 - Randomisation and python list**

# In[1]:


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end


# In[4]:


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end


# In[27]:


#randomisation
# creating random WHOLE NUMBERS

import random

random_integer = random.randint(1, 10)
print(random_integer)


# In[43]:


# creating random FLOATING POINT NUMBERS between 0 and 1
random_float = random.random()
print(random_float)


# In[57]:


# creating random FLOATING POINT NUMBERS between 0 and 5
random_float = random.random()
print(random_float)

random_float * 5


# In[66]:


love_score = random.randint(1, 100)
print(f"your love score is {love_score}")


# In[71]:


# Exercise - Heads or Tails Exercise

import random
random_side = random.randint(0, 1)
if random_side ==1:
    print("heads")
else:
    print("tails")


# **List**

# In[73]:


states_of_india = ["karnataka", "sadu", "abhi"]

print(states_of_india[0])


# In[74]:


print(states_of_india[1])


# In[75]:


print(states_of_india[-1])


# In[76]:


states_of_india[0] ="vithal"


# In[77]:


print(states_of_india[0])


# In[78]:


states_of_india.append("kishan")
print(states_of_india)


# In[79]:


states_of_india.extend(["sunitha", "ajja"])
print(states_of_india)


# In[90]:


#Coding exercise - Bank roulette - who will pay the bill?
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#getting the total number of items in list

num_items =len(names)

random_choice = random.randint(0, num_items -1)
person_who_pay = names[random_choice]
print(person_who_pay + " is going to buy the meal today")

print(len(names))
#random.randint(0, x)


# In[87]:


print(names[0])


# In[92]:


person_who_pay = random.choice(names)
print(person_who_pay + " is going to buy the meal today")


# **Nested lists**

# In[93]:


dirty_dozen = ["strawberry", "spinach", "kale", "apple", "grapes", "Peaches", "Cherries","celery", "pears","potatoes", "tomatoes"]


fruits = ["strawberry", "apple", "grapes", "Peaches", "Cherries","celery", "pears"]
vegetables = ["spinach", "kale", "potatoes", "tomatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)


# In[94]:


print(dirty_dozen[1][1])


# In[95]:


print(dirty_dozen[0])


# In[96]:


print(dirty_dozen[1])


# In[97]:


print(dirty_dozen[1][2])


# In[101]:


# Treasure Map exercise

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#23
horizontal = int(position[0])
vertical = int(position[1])

print(map[vertical-1])

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")




# In[102]:


# Treasure Map exercise

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#23
horizontal = int(position[0])
vertical = int(position[1])

selected_row= map[vertical-1]
selected_row[horizontal-1] = "X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


# In[103]:


# Treasure Map exercise

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#23
horizontal = int(position[0])
vertical = int(position[1])

selected_row= map[vertical-1]
selected_row[horizontal-1] = "X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


# In[ ]:





# In[ ]:





# In[ ]:




