import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import MaxNLocator
 

# creating the dataset
data={'1 to 3':6, '4 to 6':15, '7 to 9':10, '10 to 12':7, '13 t0 15':3, '16 to 18':3, 
        '19 to 20':3,   }
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))

ax = fig.gca()
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

 
# creating the bar plot
plt.bar(courses, values, color ='maroon', 
        width = 0.4)
 
plt.xlabel("")
plt.ylabel("")
plt.title("How many shoes do you have?")
plt.show()
