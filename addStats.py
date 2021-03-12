"""
Add some statistics series to particle df. Must have completed traacking. Must
have added dwell series to particle df if limitDwell = True.


"""
# particle df must contain exactly same particles in same order as tracking df
stats_particle = particle0      # the particle dataframe
stats_tracking = tracking       # the tracking dataframe
stats_range = (0,19)          # image range (inclusive) to analyze
limitDwell = False              # limit range for each particle individually
                                # by the dwell time

# choose which type of statistics to calculate and add
stats_shape = True   # these concern particle shape
stats_mobility = True # these concern particle dynamics

# set an index to indentify these stats in the particle df
stats_index = 0

#############################################################################
#############################################################################

# determine tracking range from tracking df, number of particles and images
track_range = (int(stats_tracking.iloc[0]['image']),int(stats_tracking.iloc[-1]['image']))
track_length = track_range[1]-track_range[0] # actually one less
numberParticles = len(stats_particle)
numberImages = stats_range[1] - stats_range[0]  + 1

# create filter to limit images considered to stats_range
print('creating filter to limit results to image range ...')
tmp=np.array( \
    [False]*stats_range[0]+[True]*numberImages+[False]*(track_length-stats_range[1]) )
statsRangeFilter = np.broadcast_to(tmp,(numberParticles,len(tmp))).transpose().flatten()

# if dwellFilter chosen, create filter to limit to images where particle is
# present, then set final filter to logical AND of the two filters
finalFilter = statsRangeFilter    # default filter
if limitDwell:
    print('creating filter to limit results by dwell time ...')
    dwelltmp= []
    for dwl in stats_particle['dwell']:
        dwelltmp.append([True]*dwl+[False]*(track_length-dwl+1) )
    dwellFilter = np.array(dwelltmp).transpose().flatten()
    finalFilter = statsRangeFilter & dwellFilter

print('applying filters, grouping and analyzing...')
addStatsGroup = stats_tracking[finalFilter].groupby('particle')
stats_mean = addStatsGroup.mean()
stats_std = addStatsGroup.std()

# create labels for series to add to particle df

stats_mean_cols = ['<xx>','<xy>','<yy>']
stats_std_cols = ['<x>', '<y>' ]
for label in stats_mean_cols:
    stats_particle[label+str(stats_index)]=stats_mean[label]
for label in stats_std_cols:
    stats_particle['s'+label+str(stats_index)]=stats_std[label]

print('SUMMARY OF RESULTS ...')
print(stats_particle.describe())