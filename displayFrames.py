"""
this script will display an array of frames

v. 2021 01 27

"""

# set frames to display
displayframes_frames = frames
                     
## use below to overide parameter values from common.py
######################################################################
displayframes_width = buffer_width              
displayframes_height = buffer_height             
displayframes_columns = columns
displayframes_rows = rows
displayframes_auto_scale = auto_scale

######################################################################
# do not change code below this line
######################################################################
######################################################################

# determine number of figs necessary
num_frames = len(displayframes_frames)
figure_count = displayframes_rows*displayframes_columns
full_figs = int(num_frames/figure_count)
print('frame count = ', num_frames)
print('frame dimensions: {}'.format(frames[0].shape))
print('display layout: {} rows X {} columns.'.format(displayframes_columns,displayframes_rows))
print( '{} frames per figure X {} figures'.format(figure_count, full_figs))
if full_figs*figure_count < num_frames:
    print( num_frames-figure_count*full_figs,'frames in last figure')

# create figures
last = 0
if num_frames >= figure_count:
    for figure in range(full_figs):

        first = figure*figure_count
        last = first + figure_count
        print( 'figure {}: frames {} to {}'.format(figure+1, first, last-1))
        pa.displayframes(displayframes_frames[first:last],rows,columns,rescale=auto_scale)

if last < num_frames:
    print( 'figure {}: frames {} to {}'.format(full_figs+1, last, num_frames-1))
    pa.displayframes(displayframes_frames[last:],rows,columns,rescale=auto_scale)

plt.show()
