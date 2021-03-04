# -*- coding: utf-8 -*-
"""
adds a column to a particle dataframe with the dwell time. The dwell time
is determined by theshold(), which determines the image number where the 
particle statistic (sum) first goes below threshold

v. 2021 02 21
"""
# particle df must contain exactly same particles in same order as tracking df
threshold_particle = particle0  # the particle dataframe
threshold_tracking = tracking   # the tracking dataframe
threshold = 400                 # threshold level

threshold_hist = True  # create histogram plot of dwell times
numbins = 80           # bins for histogram

#############################################################################
#############################################################################

# create particle grouping for thresholding
print("creating summary dataframes")
trackingGroup = threshold_tracking.groupby('particle')

# apply threshold() particle by particle
dwelllist = []
for pn in threshold_particle.index:
    data = trackingGroup.get_group(pn)[['image','sum']]
    dwelllist.append(pa.threshold(data,threshold = threshold))

# add dwell series to particle df and print summary
threshold_particle['dwell'] = dwelllist
print(threshold_particle.describe())

# plot if asked to
if threshold_hist:
    plt.figure()
    threshold_particle['dwell'].plot.hist(bins=numbins)


