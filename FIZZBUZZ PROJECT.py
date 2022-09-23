#!/usr/bin/env python
# coding: utf-8

# # FIZZBUZZ

# In[ ]:


#A code that solves the FizzBuzz problem and uses the words "GIT" and "HUB" instead of "Fizz" and "Buzz".
#It takes an input n and outputs the numbers from 1 to n.
#For each multiple of 3, it prints "GIT", instead of the number
#For each multiple of 5, it prints "HUB", instead of the number
#For numbers which are multiples of both 3 and 5, outputs "GITHUB"


# In[4]:


n = int(input("Enter a number: "))
num = list(range(1,n))
for i in num:
    #with the for loop, we iterate through the range 
    if (i%3 == 0 and i%5 == 0):
        print("GITHUB")
    elif (i%3 == 0):
        print("GIT")
    elif (i%5 == 0):
        print("HUB")
    else:
        print(n)


# In[ ]:





# In[ ]:




