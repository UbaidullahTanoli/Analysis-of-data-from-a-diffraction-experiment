#!/usr/bin/env python
# coding: utf-8

# In[1]:


#######################################################################
#By Muhammad Ubaidullah Tanoli
#######################################################################



get_ipython().run_line_magic('matplotlib', 'notebook')
import numpy as np
import matplotlib.pyplot as plt

xdata, ydata = np.loadtxt("NaCl-30kV.csv", unpack=True, delimiter=',') # importing the data from the file NaCl
plt.figure() # the plot command
x2data, y2data = np.loadtxt("LiF-30kV.csv", unpack=True, delimiter=',') # importing the data from the file LiF
plt.figure() # the plot command
plt.plot(xdata,ydata, label='NaCl') # plotting the data from NaCl
plt.plot(x2data,y2data, label='LiF') # plotting the data from LiF

plt.grid(True) # add gridlines
plt.xlim(0,130) # domain of x axis from 0 to 130
plt.ylim(0,550) # range of y axis from 0 to 550
plt.title('Data from 2 experiments of diffraction') # the title of the graph
plt.xlabel("Twice the diffraction angle (2θ), in degrees") # the variable which the horizontal axis represents
plt.ylabel('Number of counts recorded per second') # the variable which the verticle axis represents
plt.legend(loc='best'); # a key to understand the two graphs
fig = plt.figure()
fig.savefig("Graph.pdf") # saving file as pdf


# Using continous line as opossed to data points due to the large despersion and random nature of the points which would had been difficult to compare (since there are 2 graphs).
