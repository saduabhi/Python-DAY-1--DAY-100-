#!/usr/bin/env python
# coding: utf-8

# **Day 2 - python data types, and how to manipulate strings.**

# In[1]:


#Data types

#String

print("Hello"[0])


# In[2]:


print("Hello"[3])


# In[3]:


"hello"[2]


# In[6]:


"123" + "345"


# In[8]:


#Integers

123 + 456


# In[9]:


123_456_789


# In[10]:


#float

3.1456


# In[11]:


314.567


# In[15]:


#Boolean

True or False
#True and False


# In[ ]:





# In[18]:


#type error , type checking and type conversion

num_char = len(input("what is your name?"))
print(type(num_char))


# In[21]:


#type error
len(45679)


# In[20]:


#type checking

#num_char = len(input("what is your name?"))
print(type(len(input("what is your name?"))))


# In[25]:


#type conversion

num_char = len(input("what is your name?"))
new_num_char = str(num_char)

print("your name has " + new_num_char + " characters.")


# In[26]:


a = 123
type(a)


# In[27]:


a = str(123)
type(a)


# In[28]:


a = str(123)
print(type(a))


# In[29]:


print(70 + float("100.5"))


# In[30]:


print(str(70)+ str(100))


# In[33]:


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = first_digit + second_digit
print(result)


# In[34]:


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)


# In[36]:


#mathematical operation in python

3+5


# In[37]:


7-3


# In[38]:


3*2


# In[39]:


6/3


# In[41]:


2**3 #exponential


# In[42]:


5**3


# In[43]:


#Pemdas

print(3*3 + 3 / 3 - 3)


# In[44]:


print(3*(3 + 3) / 3 - 3)


# In[49]:


#BMI calculator

height = input("enter your height in mt: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) **2

print(int(bmi))


# In[50]:


#round the number of the decimal values

print(round(8/3, 2))


# In[51]:


print(8//3)


# In[52]:


result =4/2
result /=2
print(result)


# In[53]:


score =0
score +=1
print(score)


# In[54]:


score =0
score +=5
print(score)


# In[55]:


score =0
score -=5
print(score)


# In[56]:



# F-string

score = 0 
height =1.8
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


# In[60]:


# 🚨 Don't change the code below 👇
age = input("What is your current age?")

age_as_int = int(age)
years_remaining = 90-age_as_int
days_remaining = years_remaining *365
weeks_remaining = years_remaining *52
months_remaining = years_remaining *12

message = f"you have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left"

print(message)


# In[61]:


print(6 + 4 / 2 - (1 * 2))


# In[63]:


a = int("5") / int(2.7)
a


# In[ ]:




