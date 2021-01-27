"""
Analyzes an array of frames using one of these methods: 
intensity, centroid, gauss, or PCA

VARIABLE SET BY SCRIPT:
data     RESULTS OF ANALYSIS, SHAPE = (NUMFRAMES,NUMDIMENSIONS)
         WHERE NUMDIMENSIONS IS THE NUMBER OF DIMENSIONS OF DATA
         PRODUCED BY THE ANALYSIS METHOD CHOSE
         
v. 2021 01 27

"""

# here define the array of frames to analyze
analyze_frames = frames

# here define the method of tracking
analyze_method = 'pca'    # either 'intensity, 'centroid', 'gauss' or 'pca'

# if pca method is chosen, must define pca principle components here
# if other method, can leave these commented out
analyze_components =  [ V[0], V[1], V[2] ]
analyze_meanframe = meanframe

# choose to plot tracking results versus frame number also
scatter_plot = True
full_plot = True

## use below to overide parameter values from common.py
######################################################################
analyze_background = False      # set to background to use default
analyze_normalize = normalize       # set to normalize to use default

############################################################
############################################################
num_frames = len(analyze_frames)
print( num_frames, 'frames loaded for analysis.')

# subtract background if requested
if analyze_background == True:
    print("Background correction will be applied.")

# now perform tracking depending on method chosen
if analyze_method == 'intensity':
    temp = pa.statframes(analyze_frames, back = analyze_background)
    data = temp[:,0:3]
    ylabel = ['max','min','sum']

elif analyze_method == 'centroid':
    temp = pa.statframes(analyze_frames, back = analyze_background)
    data = temp[:,3:8]
    ylabel = ['<x>','<y>','<xx>','<xy>','<yy>']

elif analyze_method == 'gauss':
    data = pa.fitframes(analyze_frames, back = analyze_background)
    ylabel = ['x','y','sigma','amp','err']

elif analyze_method == 'pca':
#    meanframe = track_frames.mean(axis=0)
    data = pa.pcaframes(analyze_frames, analyze_meanframe, analyze_components)
    datadim = data.shape[1]
    ylabel = []
    for i in range(datadim):
        ylabel.append('comp {}'.format(i) )
    
else:
    print("Choose intensity, centroid, gauss or pca method.")

numpoints = len(data)
if numpoints > 0:
    print( analyze_method, 'analysis complete.', numpoints, 'frames processed.')
    print("Means of results:")
    print(data.mean(axis=0))

# create plots
if full_plot == True:
    xlabel = 'frame number'
    plot_title = analyze_method + ' analysis plots'
    pa.makeplot(data, xlabel=xlabel, ylabel=ylabel,title=plot_title)

if scatter_plot == True:
    x, y = data[:,0], data[:,1] 
    xmax, ymax = max(x), max(y)
    xmin, ymin = min(x), min(y)
    xcenter = (xmax+xmin)/2.0
    ycenter = (ymax+ymin)/2.0
    span = max( xmax-xmin, ymax-ymin )
    left = xcenter - 0.55*span
    right = xcenter + 0.55*span
    bottom = ycenter - 0.55*span
    top = ycenter + 0.55*span
    clrs = np.arange(numpoints)*255.0/numpoints

    figc, axc = plt.subplots(2,2,sharex='col',sharey='row')
    figc.suptitle(analyze_method + ' analysis scatter plot ' )
    axc[1,0].set_aspect(1.0)
    axc[1,0].set_xlim(left,right)
    axc[1,0].set_ylim(top,bottom)
    axc[1,0].scatter(x,y,c=clrs,cmap='prism',marker='.',)
    axc[1,0].grid(True)
    axc[0,0].plot(x,range(numpoints),'b.-')
    axc[1,1].plot(range(numpoints),y,'b.-')
    axc[1,0].set_xlabel('x')
    axc[1,0].set_ylabel('y')
    axc[0,0].set_ylabel('frame number')
    axc[1,1].set_xlabel('frame number')



