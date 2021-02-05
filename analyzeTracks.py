# Analyzes an array of tracks produced by trackboxes
# the data array should be set with shape (# track, # images, # data parameters)
# It calculate the mean, std and var of each data parameter and
# produces a scatter plot w/ histograms of sigmax and sigmay
#
# VARIABLE SET BY SCRIPT:
# data     RESULTS OF ANALYSIS, SHAPE = (NUMFRAMES,NUMDIMENSIONS)
#          WHERE NUMDIMENSIONS IS THE NUMBER OF DIMENSIONS OF DATA
#          PRODUCED BY THE ANALYSIS METHOD CHOSE

# here define the array of frames to analyze
tracks_data = data        # input data, use copy()

# here define the method of tracking
tracks_method = 'stats'    # only 'stats' available now

# choose what plots to generate
tracks_plot = False
tracks_scatter = True

## use below to overide parameter values from common.py
######################################################################

############################################################
############################################################
num_tracks, num_images, num_dims = tracks_data.shape
print( num_tracks, 'tracks loaded for analysis by method:', tracks_method)
print( num_images, 'time points for each track.')
print(num_dims, "dimensions of data to analyze per track.")

# now perform tracking depending on method chosen
if tracks_method == 'stats':
    data_mean = tracks_data.mean(axis=1)
    data_std = tracks_data.std(axis=1)
    data_var = tracks_data.var(axis=1)

else:
    print("Choose stats method.")

# create plots
if tracks_plot == True:
    xlabel = 'track number'
    plot_title = 'analyze tracks: plots of mean'
    pa.makeplot(data_mean, xlabel=xlabel,title=plot_title)
    plot_title = 'analyze tracks: plots standard deviation'
    pa.makeplot(data_std, xlabel=xlabel,title=plot_title)

if tracks_scatter == True:
    x, y = data_var[:,0], data_var[:,1] 
    xmax, ymax = max(x), max(y)
    xmin, ymin = min(x), min(y)
    xcenter = (xmax+xmin)/2.0
    ycenter = (ymax+ymin)/2.0
    span = max( xmax-xmin, ymax-ymin )
    left = xcenter - 0.55*span
    right = xcenter + 0.55*span
    bottom = ycenter - 0.55*span
    top = ycenter + 0.55*span
    clrs = np.arange(num_tracks)*255.0/num_tracks
    numbins = 60

    figc, axc = plt.subplots(2,2,sharex='col',sharey='row',figsize=(7,7))
    figc.suptitle('analyze tracks scatter plot ' )
    axc[1,0].set_aspect(1.0)
    axc[1,0].set_xlim(left,right)
    axc[1,0].set_ylim(top,bottom)
    axc[1,0].scatter(x,y,c=clrs,cmap='viridis',marker='.',)
    axc[1,0].grid(True)
    axc[0,0].hist(x, bins=numbins)
    axc[0,0].set_ylabel('frequency')
    axc[1,1].hist(y, bins=numbins, orientation='horizontal')
    axc[1,1].set_xlabel('frequency')
    axc[1,0].set_xlabel('sigma x')
    axc[1,0].set_ylabel('sigma y')
    


