"""
Locates isolated particles in an image or a file by finding local maxima.
Each particle should be only peak in neighborhood, whose size is given
by ROI parameters (x_buffer and y_buffer)

VARIABLE SET BY SCRIPT:
amplitudes    THE MAX INTENSITIES OF THE PEAKS FOUND IN IMAGE
xy            THE X,Y PIXEL COORDS OF PEAKS FOUND IN IMAGE

v. 2021 01 27

"""

# parameters for peak picking
minimum_value = 60     # only peaks with intensity above this are returned
maximum_number = 1000   # cut off peak finding after this number are found

# source of image for peak picking. if 'file', you must set path 
# variables below, if 'image' you must set image variables
findparticles_source = 'image'      # 'image' or 'file'
findparticles_image = image   # define image if 'image' chosen

# use below to overide parameter values from common.py
######################################################################
findparticles_directory = image_directory   # directory where image file is stored
findparticles_image_file = image_file   # name of image file
findparticles_width = buffer_width      # x buffer size for zero-ing out peak after picking
findparticles_height = buffer_height    # y buffer size for zero-ing out peak after picking
findparticles_border = border           # remove border region

######################################################################
# do not change code below this line
######################################################################
######################################################################
if findparticles_source == 'file':  
    findparticles_image_path = os.path.join(findparticles_directory,findparticles_image_file)
    findparticles_image = pa.loadim(findparticles_image_path)
    xy,amplitudes = \
        pa.findPeaks(findparticles_image,bx=findparticles_width,\
                     by=findparticles_height,maxnum=maximum_number,\
                     minval=minimum_value, border=findparticles_border)
            
    print('{} particles found using image file {}'.format(len(xy),findparticles_image_file))
    
elif findparticles_source == 'image':  
    xy,amplitudes = \
        pa.findPeaks(findparticles_image,bx=findparticles_width,\
                     by=findparticles_height,maxnum=maximum_number,
                     minval=minimum_value, border=findparticles_border)
            
    print('{} particles found using image'.format(len(xy)))

else:
    print('Set source to image or image file.')
    
    
pa.showPeaks(findparticles_image,xy)
print('maximum / minimum peak intensity: {} / {}'.format(amplitudes.max(),amplitudes.min()))
print('mean / STD peak intensity: {:3.2f} / {:3.2f}'.format(amplitudes.mean(),amplitudes.std()))

fig, ax = plt.subplots()
ax.hist(amplitudes,bins=100)
plt.title(image_path)

keys = ['x', 'y', 'maximum']

