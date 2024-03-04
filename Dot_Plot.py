import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import MaxNLocator

def dotplot(input_x, **args):
 
    # Count how many times does each value occur
    unique_values, counts = np.unique(input_x, return_counts=True)
    
    # Convert 1D input into 2D array
    scatter_x = [] # x values 
    scatter_y = [] # corresponding y values
    for idx, value in enumerate(unique_values):
        for counter in range(1, counts[idx]+1):
            scatter_x.append(value)
            scatter_y.append(counter)
 
    # draw dot plot using scatter() 
    plt.scatter(scatter_x, scatter_y, **args)
    
    # Optional - show all unique values on x-axis. 
    # Matplotlib might hide some of them  
    plt.gca().set_xticks(unique_values)

hs_heights = np.array([
    2,2,2,2,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,7,7,7,7,8,8,8,8,8,9,10,10,10,10,10,11,11,14,15,15,16,17,18,20,20
])
plt.figure(figsize=(10, 6), dpi=150)
 
dotplot(input_x=hs_heights, marker='*', color='#C44E52', s=100)
 
plt.xlabel("", fontsize=14, labelpad=15)
plt.ylabel("", fontsize=14, labelpad=15)
plt.title("How many Shoes do you have?", fontsize=14, pad=15)
plt.show()
dotplot(input_x=hs_heights)
plt.show()
