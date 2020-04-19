#!/usr/bin/env python
# coding: utf-8

# # Encodings
# 
# Encodings are a set of rules mapping string characters to their binary representations. Python supports dozens of different encoding as seen here in [this link](https://docs.python.org/3/library/codecs.html#standard-encodings). Because the web was originally in English, the first encoding rules mapped binary code to the English alphabet. 
# 
# The English alphabet has only 26 letters. But other languages have many more characters including accents, tildes and umlauts. As time went on, more encodings were invented to deal with languages other than English. The utf-8 standard tries to provide a single encoding schema that can encompass all text.
# 
# The problem is that it's difficult to know what encoding rules were used to make a file unless somebody tells you. The most common encoding by far is utf-8. Pandas will assume that files are utf-8 when you read them in or write them out.
# 
# Run the code cell below to read in the population data set.

# In[1]:


import pandas as pd
df = pd.read_csv('../data/population_data.csv', skiprows=4)


# Pandas should have been able to read in this data set without any issues. Next, run the code cell below to read in the 'mystery.csv' file.

# In[2]:


import pandas as pd
df = pd.read_csv('mystery.csv')


# You should have gotten an error: **UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte**. This means pandas assumed the file had a utf-8 encoding but had trouble reading in the data file. 
# 
# Your job in the next cell is to figure out the encoding for the mystery.csv file.

# In[4]:


# TODO: Figure out what the encoding is of the myster.csv file
# HINT: pd.read_csv('mystery.csv', encoding=?) where ? is the string for an encoding like 'ascii'
# HINT: This link has a list of encodings that Python recognizes https://docs.python.org/3/library/codecs.html#standard-encodings

# Python has a file containing a dictionary of encoding names and associated aliases
# This line imports the dictionary and then creates a set of all available encodings
# You can use this set of encodings to search for the correct encoding
# If you'd like to see what this file looks like, execute the following Python code to see where the file is located
#    from encodings import aliases
#    aliases.__file__

from encodings.aliases import aliases

alias_values = set(aliases.values())

# TODO: iterate through the alias_values list trying out the different encodings to see which one or ones work
# HINT: Use a try - except statement. Otherwise your code will produce an error when reading in the csv file
#       with the wrong encoding.
# HINT: In the try statement, print out the encoding name so that you know which one(s) worked.

for encoding in alias_values:
    try:
        pd.read_csv('mystery.csv', encoding=encoding)
        print("Successfully read the csv with encoding of ", encoding)
    except:
        print("Failed: Encoding of ", encoding)


# # Conclusion
# 
# There are dozens of encodings that Python can handle; however, Pandas assumes a utf-8 encoding. This makes sense since utf-8 is very common. However, you will sometimes come across files with other encodings. If you don't know the encoding, you have to search for it.
# 
# Note, as always, there is a solution file for this exercise. Go to File->Open.
# 
# There is a Python library that can be of some help when you don't know an encoding: chardet. Run the code cells below to see how it works.
# 

# In[5]:


# install the chardet library
get_ipython().system('pip install chardet')


# In[6]:


# import the chardet library
import chardet 

# use the detect method to find the encoding
# 'rb' means read in the file as binary
with open("mystery.csv", 'rb') as file:
    print(chardet.detect(file.read()))


# In[ ]:




