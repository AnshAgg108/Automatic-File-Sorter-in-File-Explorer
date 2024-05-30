#!/usr/bin/env python
# coding: utf-8

# In[50]:


import os, shutil 


# In[51]:


path = r"C:/Users/readi/OneDrive/Documents/Python Scripts/"


# In[52]:


file_name = os.listdir(path)


# In[53]:


folder_names = ['image files', 'text files', 'pdf files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))
        
for file in file_name:
    if ".png" in file and not os.path.exists(path + 'image files/' + file):
        shutil.move(path + file, path + 'image files/' + file)
    elif ".txt" in file and not os.path.exists(path + 'text files/' + file):
        shutil.move(path + file, path + 'text files/' + file)
    elif ".pdf" in file and not os.path.exists(path + 'pdf files/' + file):
        shutil.move(path + file, path + 'pdf files/' + file)
    #else:
        #print("There are files in this path that were not moved!")


# In[44]:





# In[ ]:




