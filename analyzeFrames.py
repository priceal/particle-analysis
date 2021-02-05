"""
Analyzes an array of frames using one of these methods: 
intensity, centroid, gauss, or PCA

VARIABLE SET BY SCRIPT:
data     RESULTS OF ANALYSIS, SHAPE = (NUMFRAMES,NUMDIMENSIONS)
         WHERE NUMDIMENSIONS IS THE NUMBER OF DIMENSIONS OF DATA
         PRODUCED BY THE ANALYSIS METHOD CHOSE
         
v. 2021 02 02

"""

# here define the array of frames to analyze
analyze_frames = frames

# here define the method of tracking
analyze_method = 'pca'    # either 'intensity, 'centroid', 'gauss' or 'pca'

# if pca method is chosen, must define pca principle components here
# if other method, can ignore these
if analyze_method == 'pca' :
    analyze_components =  [ V[0], V[1] ]
    analyze_meanframe = meanframe

# choose to plot tracking results versus frame number also
full_plot = True
scatter_plot = True
number_bins = 40   # for histograms in scatter plot

## use below to overide parameter values from common.py
######################################################################
analyze_background = background   # set to background to use default
analyze_normalize = normalize       # set to normalize to use default

############################################################
############################################################
num_frames = len(analyze_frames)
print( num_frames, 'frames loaded for analysis.')

# subtract background if requested
if analyze_background == True:
    print("Background correction will be applied.")

# set up pca_dim and pca_label for dict definition
if analyze_method == 'pca':
    pca_dim = len(analyze_components)
else:
    pca_dim = 1
pcalabel = [] 
for i in range(pca_dim):
    pcalabel.append('comp {}'.format(i) )
    
analyzeMethods = { 
    'intensity' : ['max','min','sum'],
    'centroid' : ['<x>','<y>','<xx>','<xy>','<yy>'],
    'gauss' : ['x','y','sigma','amp','err'],
    'pca' : pcalabel    }

if analyze_method in analyzeMethods.keys():

    # now perform tracking depending on method chosen
    if analyze_method == 'intensity':
        data = pa.statframes(analyze_frames, back = analyze_background)[:,0:3]
        
    elif analyze_method == 'centroid':
        data = pa.statframes(analyze_frames, back = analyze_background)[:,3:8]
        
    elif analyze_method == 'gauss':
        data = pa.fitframes(analyze_frames, back = analyze_background)
        
    elif analyze_method == 'pca':
        #    meanframe = track_frames.mean(axis=0)
        data = pa.pcaframes(analyze_frames, analyze_meanframe, \
                            analyze_components, back = analyze_background )

    numpoints = len(data)
    if numpoints > 0:
        print( analyze_method, 'analysis complete.', numpoints, 'frames processed.')
        print("Means of results:")
        print(data.mean(axis=0))

    # create plots
    if full_plot == True:
        pa.makeplot(data, xlabel = 'frame number', \
                    ylabel = analyzeMethods[analyze_method],\
                    title = analyze_method + ' analysis plots' )

    if scatter_plot == True:
        x, y = data[:,0], data[:,1] 
        xmax, ymax = max(x), max(y)
        xmin, ymin = min(x), min(y)
        xcenter = (xmax+xmin)/2.0
        ycenter = (ymax+ymin)/2.0
        span = max( xmax-xmin, ymax-ymin )

        figc, axc = plt.subplots(2,2,sharex='col',sharey='row',figsize=[7,7])
        figc.suptitle(analyze_method + ' analysis scatter plot ' )
        axc[1,0].set_aspect(1.0)
        axc[1,0].set_xlim( xcenter - 0.55*span, xcenter + 0.55*span )
        axc[1,0].set_ylim( ycenter + 0.55*span, ycenter - 0.55*span )
        axc[1,0].scatter(x,y,c = np.arange(numpoints)*255.0/numpoints,\
                         cmap='viridis',marker='.',)
        axc[1,0].grid(True)
        axc[0,0].hist(x,bins=number_bins)
        axc[1,1].hist(y,bins=number_bins,orientation='horizontal')
        axc[1,0].set_xlabel(analyzeMethods[analyze_method][0])
        axc[1,0].set_ylabel(analyzeMethods[analyze_method][1])
        axc[0,0].set_ylabel('frequency')
        axc[1,1].set_xlabel('frequency')

else:
    print("Choose intensity, centroid, gauss or pca method.")
