"""
defines common variables for particle analysis module

v. 2021 02 21

"""

# define data directory and image file range
image_directory = 'C:/Users/priceal/Desktop/DOCUMENTS/research/PROJECTS/BLT_old/BLT/rs0625'
image_range = [0, 200]

# parameters for ROI size around particles
# rectangular ROI will have size 2*width+1 X 2*height+1
buffer_width = 3           # x buffer  
buffer_height = 3            # y buffer 

# parameters for displaying ROIs
columns = 10     # number of columns in figure
rows = 10          # number of rows
auto_scale = False   # scale is 0 to 255 (False); 0 to max intensity (True)

# parameter choices for analysis. Background is subtracted before
# analysis. Normalization is after background subtraction. border = True
# will zero out a region of width/height given by buffer parameters at edge
# of images before particle finding.
background = True    # subtracts background if True
normalize = False   # normalizes frames (L1) if True
border = True       # eliminate border region when analyzing
                     
#############################################################################
#############################################################################

x_size, y_size = 2*buffer_width + 1, 2*buffer_height + 1
imageDF = pa.loadDir(image_directory)



