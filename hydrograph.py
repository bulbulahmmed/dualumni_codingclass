from matplotlib import rcParams
rcParams['font.size'] = 11
rcParams['font.sans-serif'] = ['Arial']
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import numpy as np
#
def remove_trend_from_hhead(x, y):
    """
    Purpose: Find linear trend, remove trend from the data
    --------
    Variables:
    ---------
    x : number of points
    y : hydraulic head data
    Outputs:
    --------
    It will provide hydraulic head values without the trend
    """
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    y_notrend_ft = slope * x + intercept
    y_notrend_m = (y - y_notrend_ft)/3.2808
    return y_notrend_m
#
data = pd.read_csv('hydrograph-data.txt', sep = '\t', header=None,names=['time','MW3_1','MW3_2','MW3_3','MW3_4','MW3_5','MW3_6','MW3_7','MW3_8','Precip','Precip2'])

##print data.time
data.time = pd.to_datetime(data["time"], dayfirst=True, yearfirst=False, format=None)
#data.set_index(['time'],inplace=True)
myticks=['2/18/1998','6/10/1998','8/21/1998','9/15/1998','11/12/1998','1/4/1999','2/23/1999','3/24/1999','4/27/1999','5/20/1999','6/20/1999','7/16/1999','8/31/1999']

fig, ax1 = plt.subplots(figsize=(7.5,4.25)) 
#figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

#data.set_index('time').data.MW3_1.plot()
#style = ['k-', 'k--', 'b-', 'b--', 'c-', 'g-', 'g--', 'y-']
ax1.plot(data.index, data.MW3_1/3.2808,'k-')
ax1.plot(data.index, data.MW3_2/3.2808,'k--')
ax1.plot(data.index, data.MW3_3/3.2808,'b-')
ax1.plot(data.index, data.MW3_4/3.2808,'b--')
ax1.plot(data.index, data.MW3_5/3.2808,'c-')
ax1.plot(data.index, data.MW3_6/3.2808,'g-')
ax1.plot(data.index, data.MW3_7/3.2808,'g--')
ax1.plot(data.index, data.MW3_8/3.2808,'y-')
plt.xticks(data.index, myticks, rotation=90)
ax1.set_ylabel('Head (m)')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.tick_params('y', colors='k')
#plt.legend(bbox_to_anchor=(1.0, 1.0), loc=1, borderaxespad=0.)
#ax1.legend(loc=1)
#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#           ncol=2, mode="expand", borderaxespad=0.)
#handles, labels = ax1.get_legend_handles_labels()
lgd = ax1.legend( bbox_to_anchor=(0.0, 1.02, 1., .102), loc=3,
                 ncol=4, mode="expand", borderaxespad=0.)
ax2 = ax1.twinx()
#ax2.plot(t, prec, 'r-')
ax2.plot(data.index, data.Precip/39.3701, 'ro--', label='Precipitation')
ax2.set_ylabel('Precipitation (m)', color='r')
ax2.tick_params('y', colors='r')
#fig.suptitle('Hydrograph', position=(0.5, 0.93))
#plt.legend(bbox_to_anchor=(0.0, 1.0, 1., .5), loc=4,
#           ncol=2, mode="expand", borderaxespad=0.0)
#plt.legend(bbox_to_anchor=(1.00, 0.9), loc=1, borderaxespad=0.)
ax2.legend(loc=1)
plt.tick_params(axis='both', which='major', direction='in', right=True, top=True)

fig.tight_layout()
plt.show()
fig.savefig('hydrograph.pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.close(fig)


hhead_m  = []
for i in range(1, 9, 1):
    head_m =  remove_trend_from_hhead(data.index, data.iloc[:, i])
    hhead_m.append(head_m)
#
hhead_m = np.array(hhead_m).T

labels = data.columns[1:9]
myticks=['2/18/1998','6/10/1998','8/21/1998','9/15/1998','11/12/1998','1/4/1999','2/23/1999','3/24/1999','4/27/1999','5/20/1999','6/20/1999','7/16/1999','8/31/1999']
index = range(0,13,1)
style = ['k-', 'k--', 'b-', 'b--', 'c-', 'g-', 'g--', 'y-']

fig, ax1 = plt.subplots(figsize=(7.5,4.25)) 
for i in range(0, 8, 1):
    ax1.plot(index, hhead_m[:, i], style[i], label=labels[i])
plt.xticks(data.index,myticks,rotation=90)
ax1.set_ylabel('Change in head (m)')
ax1.tick_params('y', colors='k')
handles, labels = ax1.get_legend_handles_labels()
lgd = ax1.legend( bbox_to_anchor=(0.0, 1.02, 1., .109), loc=3,
                 ncol=4, mode="expand", borderaxespad=0.)
# Second axis
ax2 = ax1.twinx()
ax2.bar(data.index, data.Precip/39.3701, width=0.4, color='red', label='Precipitation')
ax2.set_ylabel('Precipitation (m)', color='r')
ax2.tick_params('y', colors='r')
ax2.legend(loc=1)
plt.tick_params(axis='both', which='major', direction='in', right=True, top=True)

fig.tight_layout()
plt.show()
fig.savefig('hydrograph_notrend.pdf', dpi=300, bbox_extra_artists=(lgd,), bbox_inches='tight')
fig.savefig('hydrograph_notrend.png', dpi=300, bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.close(fig)
    
    
    
    
    
    
    
    
    
    
