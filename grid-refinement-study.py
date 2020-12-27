from matplotlib import rcParams
rcParams['font.size'] = 11
rcParams['font.sans-serif'] = ['Arial']
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import numpy as np
#
indx     = [1, 2, 3, 4]
times    = [340, 210, 80, 39]
gridsize = [20, 25, 50, 100]
sqheads  = [108.02, 108.10, 108.10, 108.10]

fig, ax1 = plt.subplots(figsize=(4.5, 3.25)) 
ax1.plot(gridsize, times, '-o', color='k')
ax1.set_xticks([20, 25, 50, 100])
ax1.set_xlabel('Grid dimension (m)')
ax1.set_ylabel('Time (s)')
ax1.tick_params('y', colors='k')

# Second axis
ax2 = ax1.twinx()
ax2.bar(gridsize, sqheads, width=1.0, color='red', label='Sq. difference of heads')
ax2.set_ylabel('Sq. difference of heads', color='r')
ax2.tick_params('y', colors='r')
ax2.legend()
plt.tick_params(axis='both', which='major', direction='in', right=True, top=True)

fig.tight_layout()
plt.show()
fig.savefig('grd_refinement.pdf', dpi=300, bbox_inches='tight')
fig.savefig('grd_refinement.png', dpi=300, bbox_inches='tight')
plt.close(fig)
    
    
    
    
    
    
    
    
    
    
