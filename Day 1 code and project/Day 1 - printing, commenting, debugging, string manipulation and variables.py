#!/usr/bin/env python
# coding: utf-8

# **Day 1 - python printing, commenting, Debugging, String manipulation and variables**

# In[1]:


print('Day1 - Python print function')   #printing
print('the function is declared like this')
print("print('what to print')")      


# In[2]:


#String manipulation and code intelligence
print('hello sadu\nhello sadu')


# In[3]:


#concatenate- combining different strings so that will be added to the end of another strings.
print("hello" + "sadu")
print("hello" +" "+"sadu")


# In[4]:


#Debugging
print("Day 1 -string Manipulation")
print("string concatenation is done with '+' sign.")
print('e.g print("hello" + "world")')
print("new lines can be created with backslash and n.")


# In[5]:


#input infunction
input("hii man, how are you?")


# In[6]:


print("hello " + input("what is your name?"))


# In[7]:


#Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.
input("what is your name?")

print(len("Angela"))


# In[8]:


print( len(input("what is your name?")))


# In[9]:


#python variables
name = input("what is your name?")
print(name)


# In[11]:


name= "sadu"
print(name)

name= "abhi"
print(name)


# In[12]:


name = input("what is your name?")
length = len(name)

print(length)


# In[13]:


# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a =b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


# **project 1 - Band name generator**

# In[20]:


#create the greeting for the program
print("Welcome to the Band name generator")

#asking the user in which city did they grew up
city = input("what city did you grew up?\n")
#print(city)

#asking the user about their pet name
pet_name = input("what is your pet name?\n")
#print(pet_name)

#combine the name of their city and pet name and show them their band name
print("Your band name could be " + city + " " + pet_name)

#make sure that the input cursor shows on the next or new line


# In[ ]:





# In[ ]:




