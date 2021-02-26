# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 08:58:46 2021

@author: priceal
"""

analyze_shape_stats = True
analyze_mobility_stats = True
numbins = 100

stats_index = 1
stats_range = (10,18)

stats_particle = particle0[:3]

stats_tracking = tracking

duration = 200

#############################################################################
#############################################################################



# create the filter

numberParticles = len(stats_particle)
numberImages = stats_range[1] - stats_range[0] + 1

tmp = [False]*stats_range[0]+[True]*numberImages+[False]*(duration-stats_range[1])
temprange = np.array( tmp * numberParticles)

tmp2 = []
for dwl in stats_particle['dwell']:
    print(dwl)
    temp2 += [True]*dwl+[False]*(duration-dwl)

