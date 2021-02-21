# -*- coding: utf-8 -*-
"""
adds a column to a particle dataframe with the dwell time. The dwell time
is determined by theshold(), which determined the image number of the last
image where the particle statistic (sum) is above threshold level.

v. 2021 02 21
"""

threshold_particle = particle0  # the particle dataframe
threshold_tracking = tracking   # the tracking dataframe
threshold = 200                 # threshold level

threshold_hist = True  # create histogram plot of dwell times

#############################################################################
#############################################################################

# create plots
print("creating summary dataframes")
trackingGroup = threshold_tracking.groupby('particle')
dwelllist = []

for pn in threshold_particle.index:
    data = trackingGroup.get_group(pn)[['image','sum']]
    dwelllist.append(pa.threshold(data,threshold = threshold))
  
threshold_particle['dwell'] = dwelllist
plt.figure()
threshold_particle['dwell'].plot.hist(bins=50)
print(threshold_particle.describe())
