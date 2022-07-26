#!/usr/bin/env python
# coding: utf-8

# **Day 5 - For loops, Range and code blocks**

# In[1]:


fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# In[2]:


fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
    print(fruit  + " pie")


# In[3]:


fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
    print(fruit  + " pie")
    print(fruits)


# In[4]:


fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
    print(fruit  + " pie")
print(fruits)


# In[6]:


# COding Exercise = The Average Height

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

print(len(student_heights))
print(sum(student_heights))


# In[7]:


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height/number_of_students)
print(average_height)



# In[10]:


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)


number_of_students = 0
for students in student_heights:
    number_of_students += 1
print(number_of_students)


average_height = round(total_height/number_of_students)
print(average_height)



# In[12]:


# COding Exercise = The highest score exercise

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
print(max(student_scores))
print(min(student_scores))


# In[14]:


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score =0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"the highest score is: {highest_score}")


# In[15]:


#For loop with range

for number in range(1, 10):
    print(number)



# In[16]:



for number in range(1, 11):
    print(number)


# In[17]:



for number in range(1, 11, 3):
    print(number)


# In[19]:


# adding all the numbers starting from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)


# In[20]:


# Coding exercise adding even numbers
# calculating the sum of even numbers from 1 to 100 , including 1 and 100.

total = 0
for number in range(2, 101, 2):
    total += number
print(total)


# In[21]:


total2 = 0
for number in range(1, 101):
    if number % 2 ==0:
        total2 += number
print(total2)


# In[22]:


# coding exercise- Fizz Buzz Exercise 


#You are going to write a program that automatically prints the solution to the FizzBuzz game.

#Your program should print each number from 1 to 100 in turn.

#When the number is divisible by 3 then instead of printing the number it should print "Fizz".

#When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

#And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`


for number in range(1, 101):
    if number % 3==0 and number % 5==0:
        #Divisible by 3 and 5
        print("FizzBuzz")
    elif number % 3 ==0:
        print("Fizz")
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(number)




# In[ ]:





# In[ ]:




