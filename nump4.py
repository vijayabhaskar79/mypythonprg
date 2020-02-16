import numpy as np
import matplotlib.pyplot as plt
'''
roc_t = 0.43652219
roc_v = 0.82251961

plt.figure()
plt.figure(figsize=(15,12))
plt.xlim(-0.2,1.4)
plt.ylim(-0.2,1.4)
plt.scatter([nTPredict], [nVPredict], color = 'red', marker='X', s=500)

plt.plot([T_Cutoff,T_Cutoff],[-0.2,1.4],color = 'black',linestyle='dashed',lw=2)
plt.plot([1.4,-0.2],[(V_Cutoff),(V_Cutoff)],color = 'black',linestyle='dashed',lw=2)

plt.axvspan(-0.2, roc_t, 0, roc_v, alpha=0.3, color='#1F98D0')#blue
plt.axvspan(roc_t, 1.4, 0, roc_v, alpha=0.3, color='#F9D307')#yellow
plt.axvspan(-0.2, roc_t, roc_v, 1, alpha=0.3, color='#F38D25')#orange
plt.axvspan(roc_t, 1.4, roc_v, 1, alpha=0.3, color='#DA383D')#red

plt.show()
plt.close()
'''

roc_t = 0.43652219
roc_v = 0.82251961

T_Cutoff = roc_t
V_Cutoff = roc_v

fig,ax = plt.subplots(figsize=(15,12))
ax.set_xlim(-0.2,1.4)
ax.set_ylim(-0.2,1.4)


ax.axvline(T_Cutoff,color = 'black',linestyle='dashed',lw=2)
ax.axhline(V_Cutoff,color = 'black',linestyle='dashed',lw=2)

ax.fill_between([-0.2, roc_t],-0.2,roc_v,alpha=0.3, color='#1F98D0')  # blue
ax.fill_between([roc_t, 1.4], -0.2, roc_v, alpha=0.3, color='#F9D307')  # yellow
ax.fill_between([-0.2, roc_t], roc_v, 1.4, alpha=0.3, color='#F38D25')  # orange
ax.fill_between([roc_t, 1.4], roc_v, 1.4, alpha=0.3, color='#DA383D')  # red

plt.show()
