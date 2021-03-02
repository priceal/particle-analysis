"""
Add some statistics series to particle df. Must have completed traacking. Must
have added dwell series to particle df if XXXX chosen.


"""
# particle df must contain exactly same particles in same order as tracking df
stats_particle = particle0      # the particle dataframe
stats_tracking = tracking       # the tracking dataframe
stats_range = (0,99)          # image range (inclusive) to analyze
limitDwell = True              # limit range for each particle individually
                                # by the dwell time

# choose which type of statistics to calculate and add
analyze_shape_stats = True    # these concern particle shape
analyze_mobility_stats = True # these concern particle dynamics

#############################################################################
#############################################################################

# determine tracking range from tracking df, number of particles and images
track_range = (int(stats_tracking.iloc[0]['image']),int(stats_tracking.iloc[-1]['image']))
track_length = track_range[1]-track_range[0] # actually one less
numberParticles = len(stats_particle)
numberImages = stats_range[1] - stats_range[0]  + 1

# create filter to limit images considered to stats_range
tmp=np.array( \
    [False]*stats_range[0]+[True]*numberImages+[False]*(track_length-stats_range[1]) )
statsRangeFilter = np.broadcast_to(tmp,(numberParticles,len(tmp))).transpose().flatten()

if limitDwell:
    dwelltmp= []
    for dwl in stats_particle['dwell']:
        dwelltmp.append([True]*dwl+[False]*(track_length-dwl+1) )
    dwellFilter = np.array(dwelltmp).transpose().flatten()
    finalFilter = statsRangeFilter & dwellFilter


