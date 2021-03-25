"""
plots tracks of all particles in a grid. will limit by dwell time to not plot
points after bead goes away. scale of each plot is set by width and height.
each plot shows x values from mean-width to mean+width. Similar for height.
value of 1 seems to be good choice.

v. 2021 03 19
"""

# define particls and tracking
displayTracks_particle = particle0
displayTracks_group = trackingGroup

# define range of images to use
displayTracks_range = (90,599)

# define plot size, 1 is good choice
displayTracks_width = 1         
displayTracks_height = 1     
                     
## use below to overide parameter values from common.py
######################################################################
displayTracks_columns = columns
displayTracks_rows = rows
######################################################################
# do not change code below this line
######################################################################
######################################################################

# determine number of figs necessary
num_tracks = len(displayTracks_particle)
figure_count = displayTracks_rows*displayTracks_columns
full_figs = int(num_tracks/figure_count)
print('track count = ', num_tracks)
print('track plot dimensions: {} x {}'.format(2*displayTracks_width,2*displayTracks_height))
print('display layout: {} rows X {} columns.'.format(displayTracks_columns,displayTracks_rows))
print( '{} tracks per figure X {} figures'.format(figure_count, full_figs))
if full_figs*figure_count < num_tracks:
    print( num_tracks-figure_count*full_figs,'tracks in last figure')

# create figures
dwellLimit = displayTracks_particle['dwell']
last = 0
df_count = 0
if num_tracks >= figure_count:
    for figure in range(full_figs):

        first = figure*figure_count
        last = first + figure_count
        print( 'figure {}: tracks {} to {}'.format(figure+1, first, last-1))

        fig, ax = plt.subplots(displayTracks_rows,displayTracks_columns)
        ax_flatten = ax.flatten()
        for ax_count in range(figure_count):
            pdf = displayTracks_group.get_group(df_count)
            images = pdf['image'].to_numpy()
            limits = (images < dwellLimit[df_count]) & (images < displayTracks_range[1]) & (images > displayTracks_range[0])
            pdfLimited = pdf[ limits ]
            pdfLimited.plot.scatter(x='x',y='y',marker='.',ax=ax_flatten[ax_count])
            xCenter = pdfLimited['x'].mean(); yCenter = pdfLimited['y'].mean()
            if np.isnan(xCenter) or np.isnan(yCenter):
                xCenter, yCenter = 0, 0
        
            ax_flatten[ax_count].set_xticks([]); ax_flatten[ax_count].set_yticks([])
            ax_flatten[ax_count].set_xlabel(''); ax_flatten[ax_count].set_ylabel('')
            ax_flatten[ax_count].set_aspect('equal')
            ax_flatten[ax_count].set_xlim((xCenter-displayTracks_width,xCenter+displayTracks_width))
            ax_flatten[ax_count].set_ylim((yCenter-displayTracks_height,yCenter+displayTracks_height))
            df_count += 1 
        
if last < num_tracks:
    print( 'figure {}: tracks {} to {}'.format(full_figs+1, last, num_tracks-1))
#    pa.displayframes(displayframes_frames[last:],rows,columns, \
#                     rescale = displayframes_auto_scale)
    fig, ax = plt.subplots(displayTracks_rows,displayTracks_columns)
    ax_flatten = ax.flatten()
    for ax_count in range(num_tracks-figure_count*full_figs):
        pdf = displayTracks_group.get_group(df_count)
        images = pdf['image'].to_numpy()
        limits = (images < dwellLimit[df_count]) & (images < displayTracks_range[1]) & (images > displayTracks_range[0])
        pdfLimited = pdf[ limits ]
        pdfLimited.plot.scatter(x='x',y='y',marker='.',ax=ax_flatten[ax_count])
        xCenter = pdfLimited['x'].mean(); yCenter = pdfLimited['y'].mean()
        if np.isnan(xCenter) or np.isnan(yCenter):
            xCenter, yCenter = 0, 0
        ax_flatten[ax_count].set_xticks([]); ax_flatten[ax_count].set_yticks([])
        ax_flatten[ax_count].set_xlabel(''); ax_flatten[ax_count].set_ylabel('')
        ax_flatten[ax_count].set_aspect('equal')
        ax_flatten[ax_count].set_xlim((xCenter-displayTracks_width,xCenter+displayTracks_width))
        ax_flatten[ax_count].set_ylim((yCenter-displayTracks_height,yCenter+displayTracks_height))          
        df_count += 1 


