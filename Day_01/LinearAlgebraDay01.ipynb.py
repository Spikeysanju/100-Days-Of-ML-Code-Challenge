
# coding: utf-8

# In[2]:


get_ipython().run_cell_magic('HTML', '', '<h1>#100DaysOfMLCode</h1>\n')


# In[9]:


import numpy as np
import matplotlib.pyplot as plt
N = 150
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2
plt.scatter(x,y,s=area,c=colors,alpha=10)
plt.show()

