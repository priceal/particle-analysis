# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 08:58:46 2021

@author: priceal
"""

analyze_shape_stats = True
analyze_mobility_stats = True
numbins = 100

stats_index = 1
stats_range = (92,140)  # inclusive range

stats_particle = particle140

stats_tracking = tracking


#############################################################################
#############################################################################

# determine tracking range
track_range = (int(stats_tracking.iloc[0]['image']),int(stats_tracking.iloc[-1]['image']))
track_length = track_range[1]-track_range[0] # actually one less

# create the filter
numberParticles = len(stats_particle)
numberImages = stats_range[1] - stats_range[0]  + 1

tmp=np.array( \
    [False]*stats_range[0]+[True]*numberImages+[False]*(track_length-stats_range[1]) )
    
temprange = np.broadcast_to(tmp,(numberParticles,len(tmp)))
finalrange = temprange.transpose().flatten()




addStatsGroup = stats_tracking[finalrange].groupby('particle')


#tmp2 = []
#for dwl in stats_particle['dwell']:
#    print(dwl)
#    temp2 += [True]*dwl+[False]*(duration-dwl)

