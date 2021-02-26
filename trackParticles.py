"""
Tracks a set of particles across a stack of images. The particle locations
are stored in track_xy and the source is given in the default imageDF.

VARIABLES SET BY SCRIPT:
tracking  a data frame with tracking results with following columns:
            "particle" : particle number
            "image" :   image number
            "max" :     mas intensity in ROI
            "min" :     min intensity in ROI
            "sum" :     sum of intensities in ROI
            "<x>" :     mean x
            "<y>" :     mean y
            "<xx>" :    mean xx
            "<xy>" :    mean xy
            "<yy>" :    mean yy

trackingGroup     above dataframe grouped by particle number

v. 2021 02 21

"""
# define particle dataframe (contains x,y coords of particles)
track_xy = particle140

# define any peaks to exclude
track_exclude = False
if track_exclude:
    exclude_xy = xy599

#if you want plots, set to True
track_plots = True
if track_plots:
    plotcols = ["sum" , "<x>", "<y>"]

## use below to overide parameter values from common.py
######################################################################
track_width = buffer_width              
track_height = buffer_height
track_range = image_range     # inclusive range
track_background = background
track_normalize = normalize
######################################################################

# do not change code below this line
######################################################################
######################################################################
tracking = pd.DataFrame ( {
    "particle" : [],
    "image" : [],
    "max" : [],
    "min" : [],
    "sum" : [],
    "<x>" : [],
    "<y>" : [],
    "<xx>" : [],
    "<xy>" : [],
    "<yy>" : []
    } )

# exclude particles if asked to
if track_exclude:
    track_xy = pa.subtractxy(track_xy,exclude_xy,bx=buffer_width,by=buffer_height)
    
# define some arrays needed to form data frame
print("processing images..." )
particleNums = track_xy.index.to_numpy()[:,np.newaxis]
ones_column = np.ones(len(particleNums))[:,np.newaxis]

# perform tracking
count = 0
for image in range(track_range[0],track_range[1]+1):
    temp_frames = pa.cropframes(image,track_xy,bx=track_width,by=track_height,\
                                imgDF = imageDF)
    # create correct format of array and append to dataframe
    temp_data = pa.statframes_(temp_frames, back = track_background)
    append_data = np.concatenate((particleNums,image*ones_column,temp_data),axis=1)
    append_df = pd.DataFrame(data=append_data,columns=tracking.columns)
    tracking = tracking.append(append_df,ignore_index=True)
    
    # print status every 50 images
    count += 1
    if count == 51:
        print("    ... image number {}: {} ".format(image,imageDF['path'][image]))
        count = 1
   
trackingGroup = tracking.groupby('particle')
         
print("processed {} images X {} particles each = {} ROIs".\
      format(track_range[1]-track_range[0],len(track_xy),len(tracking)))
print('SUMMARY OF RESULTS: tracking')
print(tracking.describe())

# plot results if asked to
if track_plots:
    fig,ax = plt.subplots(len(plotcols),1)
    [ ax[i].set_ylabel(plotcols[i]) for i in range(len(plotcols)) ]
    for pn in track_xy.index:
        trackingGroup.get_group(pn)[plotcols+['image']].\
                        plot(x='image',subplots=True,ax =ax, legend=False)
 