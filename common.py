"""
defines common variables for particle analysis module

v. 2021 01 27

"""

# define data directory and primary image file
image_directory = 'C:/Users/priceal/Desktop/DOCUMENTS/research/PROJECTS/BLT_old/BLT/E51'
image_file = 'E51_020.jpg'
image_range = [0, 250]

# parameters for ROI size around particles
# rectangular ROI will have size 2*width+1 X 2*height+1
buffer_width = 3           # x buffer zone  
buffer_height = 3            # y buffer zone 

# parameters for displaying ROIs
columns = 10     # number of columns in figure
rows = 10          # number of rows
auto_scale = True   # scale is 0 to 255 (False); 0 to max intensity (True)

# parameter choices for analysis. Background is subtracted before
# analysis. Normalization is after background subtraction.
background = True    # subtracts background if True
normalize = False   # normalizes frames (L1) if True
border = True       # eliminate border region when analyzing
                     
############################################################
x_size, y_size = 2*buffer_width + 1, 2*buffer_height + 1
image_path = os.path.join(image_directory,image_file)




