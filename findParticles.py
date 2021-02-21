"""
Locates isolated particles in an image or a file by finding local maxima.
Each particle should be only peak in neighborhood, whose size is given
by ROI parameters (x_buffer and y_buffer)

VARIABLE SET BY SCRIPT:
xyN         data frame containing the X,Y PIXEL COORDS OF PARTICLES FOUND 
            and the intensities of the peaks, N is the image number

v. 2021 02 13

"""
# parameters for peak picking
minimum_value = 10    # only peaks with intensity above this are returned
maximum_number = 1000   # cut off peak finding after this number are found
# image number to use for picking
findparticlesImageNumber = 0

# for particle filtering added as a pre-filter
findparticles_prefilter = False
if findparticles_prefilter:
    sigma = 2.0 # smoothing HWHH
    dims = (11,11) # window size for particle filter kernel
    norm = 3.0    # normalization for +kernal portion

    
# use below to overide parameter values from common.py
######################################################################
findparticles_width = buffer_width      # x buffer size for zero-ing out peak after picking
findparticles_height = buffer_height    # y buffer size for zero-ing out peak after picking
findparticles_border = border           # remove border region
findparticles_imageDF = imageDF         # dataframe containing list of image file paths
######################################################################

# do not change code below this line
######################################################################
######################################################################
# if pre-filtering, load and filter image, set findparticlesImage to the 
# filtered image. If not, set findparticlesImage = findparticlesImageNumber
if findparticles_prefilter:
    image = pa.loadim( imageDF['path'][findparticlesImageNumber] )
    findparticlesImage = pa.particleFilter(image,sigma,dims,norm=norm)
else:
    findparticlesImage = findparticlesImageNumber
    
# create the data frame to hold results
findparticles_output = 'particle' + str(findparticlesImageNumber)
print( 'creating DataFrame ' + findparticles_output + ' ...')
exec( findparticles_output + ' = pd.DataFrame( { "x" : [], "y" : [], \
                             "intensity" : [] } )' )

# call particle finding function and report summary of results
print('finding particles in image {}: {} ...'.\
      format(findparticlesImageNumber,imageDF['path'][findparticlesImageNumber]) )
pa.findPeaks(findparticlesImage, eval(findparticles_output), imgDF = imageDF, \
             bx=findparticles_width, by=findparticles_height, \
             maxnum=maximum_number, minval=minimum_value, \
             border=findparticles_border)
print('SUMMARY OF RESULTS: ' + findparticles_output)
print(eval(findparticles_output).describe())

# create plots for evaluation
pa.showPeaks(findparticlesImage, \
             eval(findparticles_output)[['x','y']].to_numpy(), imgDF = imageDF )
eval(findparticles_output).hist(column='intensity',bins=50)
