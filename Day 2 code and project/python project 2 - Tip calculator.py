#!/usr/bin/env python
# coding: utf-8

# **python project 2 - Tip calculator.**

# In[69]:


print("welcome to the tip calculator!")
bill=float(input("what was the total bill? $"))
tip=int(input("how much tip would you like to give? 10, 12, 15?"))
people = int(input("how many people are splitting the bill?"))
tip_as_percent = tip/100 
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"each person should pay ${final_amount}")


# In[70]:


print("welcome to the tip calculator!")
bill=float(input("what was the total bill? $"))
tip=int(input("how much tip would you like to give? 10, 12, 15?"))
people = int(input("how many people are splitting the bill?"))
tip_as_percent = tip/100 
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"each person should pay ${final_amount}")


# In[ ]:





# In[ ]:





# In[ ]:




