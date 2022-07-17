#!/usr/bin/env python
# coding: utf-8

# **Day 3 - Conditional statements, code blocks and scope and Logical opearators**

# **if - else statement**

# In[4]:


# control flow- if/else statement 
# example - bath tub
water_level =50
if water_level > 80:
    print("Drain water")
else:
    print("continue")


# In[5]:


#tickets

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height > 120:
    print("you can ride the rollercoaster")
else:
    print("you cannot ride the rollercoaster because you are short")


# In[6]:


#tickets

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height > 120:
    print("you can ride the rollercoaster")
else:
    print("you cannot ride the rollercoaster because you are short")


# In[18]:


#tickets

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoaster")
else:
    print("you cannot ride the rollercoaster because you are short")


# In[11]:


#tickets

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height == 120:
    print("you can ride the rollercoaster")
else:
    print("you cannot ride the rollercoaster because you are short")


# In[16]:


#tickets

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height != 120:
    print("you can ride the rollercoaster")
else:
    print("you cannot ride the rollercoaster because you are short")


# In[15]:


#tickets

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height != 120:
    print("you can ride the rollercoaster")
else:
    print("you cannot ride the rollercoaster because you are short")


# In[26]:


#coding exercise

7 % 2 


# In[27]:


7 % 4 # modulus gives the remainder


# In[32]:



# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 ==0:
    print("this is even number")
else:
    print("this is odd number")


# In[33]:



# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 ==0:
    print("this is even number")
else:
    print("this is odd number")


# **nested if and elif statements**

# In[37]:


#tickets

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age< 12:
        print("please pay $5")
    elif age<= 18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
    print("you cannot ride the rollercoaster because you are short")


# In[38]:


#tickets

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age< 12:
        print("please pay $5")
    elif age<= 18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
    print("you cannot ride the rollercoaster because you are short")


# In[40]:


#coding exercise

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight/ height **2)
if bmi<18.5:
    print(f"your bmi is {bmi}, you are under weight.")
elif bmi<25:
    print(f"your bmi is {bmi}, you have a Normal weight.")
elif bmi<30:
    print(f"your bmi is {bmi}, you are over weight.")
elif bmi<35:
    print(f"your bmi is {bmi}, you are obese.")
else:
    print(f"your bmi is {bmi}, you are clinically obese.")


# In[41]:


#coding exercise

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight/ height **2)
if bmi<18.5:
    print(f"your bmi is {bmi}, you are under weight.")
elif bmi<25:
    print(f"your bmi is {bmi}, you have a Normal weight.")
elif bmi<30:
    print(f"your bmi is {bmi}, you are over weight.")
elif bmi<35:
    print(f"your bmi is {bmi}, you are obese.")
else:
    print(f"your bmi is {bmi}, you are clinically obese.")


# In[43]:


bmi = 25
if bmi<18.5:
    print(f"your bmi is {bmi}, you are under weight.")
elif bmi<25:
    print(f"your bmi is {bmi}, you have a Normal weight.")
elif bmi<30:
    print(f"your bmi is {bmi}, you are over weight.")
elif bmi<35:
    print(f"your bmi is {bmi}, you are obese.")
else:
    print(f"your bmi is {bmi}, you are clinically obese.")


# In[45]:


# coding exercise - Leap Year exercise
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not leap year")


# In[46]:


# coding exercise - Leap Year exercise
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not leap year")


# **multiple if statements**

# In[49]:


#tickets

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0
if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age< 12:
        bill = 5
        print("child tickets are $5")
    elif age<= 18:
        bill = 7
        print("youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    
    wants_photo = input("Do you want a photo to be taken? Y or N. ")
    if wants_photo == "Y":
        bill = bill + 3  # adding 3$ to bill
        #or it can be written as bill +=3
    print(f"your final bill is {bill}")
    
else:
    print("you cannot ride the rollercoaster because you are short")


# In[51]:


#pizza order exercise
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill =0

if size == "S":
    bill +=15
elif size == "M":
    bill +=20
elif size == "L":
    bill +=25

if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3
        
if extra_cheese =="Y":
    bill +=1
    
print(f"your final bill is ${bill}")


# In[52]:


# Logical opearors

a=12
a>10


# In[53]:


a =10
a>9 and a< 12 


# In[54]:


a =10
not a >15


# In[55]:


#tickets

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0
if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age?"))
    if age< 12:
        bill = 5
        print("child tickets are $5")
    elif age<= 18:
        bill = 7
        print("youth tickets are $7")
    elif age>=45 and age<=55:
        print("everything is ok, have a free ride on us")
    else:
        bill = 12
        print("Adult tickets are $12")
    
    wants_photo = input("Do you want a photo to be taken? Y or N. ")
    if wants_photo == "Y":
        bill = bill + 3  # adding 3$ to bill
        #or it can be written as bill +=3
    print(f"your final bill is {bill}")
    
else:
    print("you cannot ride the rollercoaster because you are short")


# In[67]:


# Love calculator exercise

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1+name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t+r+u+e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l+o+v+e

love_score = int(str(true) + str(love))
#int_score = int(love_score)
if (love_score < 9) or (love_score > 90):
    print(f"your love score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"your love score is {love_score}, you are alright together")
else:
    print(f"your love_score is {love_score}")


# In[ ]:





# In[ ]:





# In[ ]:




