#!/usr/bin/env python
# coding: utf-8

# **Python project 4 -Rock paper scissors**

# **RULES-
# *0) Rock wins against scissors  
# 2)scissor wins against papers  
# 1)paper wins against rock**

# In[2]:


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

#Write your code below this line 👇
print(rock)
print(paper)
print(scissors)


# In[33]:


import random

game_images = [rock, paper, scissors]
user_choice = int(input("what do you want to choose? type 0 for rock, 1 for paper and 2 for scissors "))


if user_choice >=3 or user_choice <0:
    print("you typed invalid number")
else:
    print(game_images[computer_choice])

computer_choice = random.randint(0,2)
print(f"computer chose:")
print(game_images[user_choice])

if user_choice ==0 and computer_choice ==2:
    print("you win")
elif computer_choice ==0 and user_choice ==2:
    print("you win")
elif computer_choice > user_choice:
    print("computer wins or you lose")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("its a draw")
elif user_choice >=3 or user_choice <0:
    print("you typed invalid number")


# In[34]:


import random

game_images = [rock, paper, scissors]
user_choice = int(input("what do you want to choose? type 0 for rock, 1 for paper and 2 for scissors "))


if user_choice >=3 or user_choice <0:
    print("you typed invalid number")
else:
    print(game_images[computer_choice])

computer_choice = random.randint(0,2)
print(f"computer chose:")
print(game_images[user_choice])

if user_choice ==0 and computer_choice ==2:
    print("you win")
elif computer_choice ==0 and user_choice ==2:
    print("you win")
elif computer_choice > user_choice:
    print("computer wins or you lose")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("its a draw")
elif user_choice >=3 or user_choice <0:
    print("you typed invalid number")


# In[36]:


import random

game_images = [rock, paper, scissors]
user_choice = int(input("what do you want to choose? type 0 for rock, 1 for paper and 2 for scissors "))


if user_choice >=3 or user_choice <0:
    print("you typed invalid number")
else:
    print(game_images[computer_choice])

computer_choice = random.randint(0,2)
print(f"computer chose:")
print(game_images[user_choice])

if user_choice ==0 and computer_choice ==2:
    print("you win")
elif computer_choice ==0 and user_choice ==2:
    print("you win")
elif computer_choice > user_choice:
    print("computer wins or you lose")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("its a draw")
elif user_choice >=3 or user_choice <0:
    print("you typed invalid number")


# In[37]:


import random

game_images = [rock, paper, scissors]
user_choice = int(input("what do you want to choose? type 0 for rock, 1 for paper and 2 for scissors "))


if user_choice >=3 or user_choice <0:
    print("you typed invalid number")
else:
    print(game_images[computer_choice])

computer_choice = random.randint(0,2)
print(f"computer chose:")
print(game_images[user_choice])

if user_choice ==0 and computer_choice ==2:
    print("you win")
elif computer_choice ==0 and user_choice ==2:
    print("you win")
elif computer_choice > user_choice:
    print("computer wins or you lose")
elif user_choice > computer_choice:
    print("you win")
elif computer_choice == user_choice:
    print("its a draw")
elif user_choice >=3 or user_choice <0:
    print("you typed invalid number")


# In[ ]:





# In[ ]:





# In[ ]:




