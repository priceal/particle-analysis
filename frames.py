"""
creates an array of frames using image or source and xy array

VARIABLE SET BY SCRIPT:
frames    AN ARRAY OF 2D FRAMES

v. 2021 01 27

"""


# source of image(s) for frames. if 'file', you must set path 
# variables below, if 'image' you must set image variable here
# if 'directory' you are intending to create a time history of
# a single particle throughout the image files in the directory
frames_source = 'image'      # 'image' or 'file' or 'directory'
frames_image = image         # define image if 'image' chosen

# define array of frame centers (xy) cropping multiple boxes from a 
# single image for 'image' and 'file' option. Define a single [x,y] 
# if you are cropping a single box from multiple image files stored 
# in frames_directory---this option is for creating a time history 
# of a single particle
frames_xy = xy
#frames_xy = xy[100]

## use below to overide parameter values from common.py
######################################################################
frames_directory = image_directory
frames_image_file = image_file
frames_width = buffer_width              
frames_height = buffer_height
frames_range = image_range

######################################################################
# do not change code below this line
######################################################################
######################################################################
if frames_source == 'file':
    frames_image_path = os.path.join(frames_directory,frames_image_file)
    frames_image = pa.loadim(frames_image_path)
    frames = \
        pa.cropframes(frames_image,frames_xy,bx=frames_width,by=frames_height)
    print("{} frames made from image file ".format(len(frames)) + frames_image_file)
        
elif frames_source == 'image':
    frames = \
        pa.cropframes(frames_image,frames_xy,bx=frames_width,by=frames_height)
    print("{} frames made from image.".format(len(frames)))

elif frames_source == 'directory':
    frames = \
        pa.cutframe_file(frames_xy,bx=frames_width,by=frames_height,data=frames_directory,rang=frames_range)
    print("{} frames made from directory".format(len(frames)) + frames_directory)

else:
    print("No frames made. Choose source: file, image or directory.")     
    
print('frame dimensions: {}'.format(frames[0].shape))

        