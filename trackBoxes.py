"""
Analyzes a set of particles across a stack of images. The particle locations
are stored in boxes_xy and the source is given in the boxes_directory.

VARIABLE SET BY SCRIPT:
data   AN ARRAY OF ANALYSIS RESULTS OF FORM:
       data[PARTICLE #, TIME STAMP, data dimension]    
             
v. 2021 02 02

"""

# source of images. if 'files', you must set path variables below
boxes_source = 'files'      # only 'files' available for now

# define boxes xy ---list of centers of boxes
boxes_xy = xy[:10]

# define tracking method
boxes_method = 'pca'  # either 'intensity, 'centroid', 'gauss' or 'pca'

# if pca method is chosen, must define pca principle components here
# if other method, can leave these commented out
principle_components =   [ V[0],V[1],V[2],V[3] ] 
boxes_meanframe = meanframe

## use below to overide parameter values from common.py
######################################################################
boxes_directory = image_directory
boxes_width = buffer_width              
boxes_height = buffer_height
boxes_image_range = image_range
boxes_background = background
boxes_normalize = normalize

######################################################################
# do not change code below this line
######################################################################
######################################################################
dir_list = os.listdir(boxes_directory)
dir_list_sorted = pa.heapsort(dir_list)

# set up pca_dim and pca_label for ylabels definition
if boxes_method == 'pca':
    pca_dim = len(principle_components)
else:
    pca_dim = 1
pcalabel = [] 
for i in range(pca_dim):
    pcalabel.append('comp {}'.format(i) )
    
ylabels = { 
    'intensity' : ['max','min','sum'],
    'centroid' : ['<x>','<y>','<xx>','<xy>','<yy>'],
    'gauss' : ['x','y','sigma','amp','err'],
    'pca' : pcalabel    }

if boxes_method in ylabels.keys():
    
    #     now perform tracking depending on method chosen
    listall = []
    print(" images from", boxes_directory )
    count = 0
    for file in dir_list_sorted[boxes_image_range[0]:boxes_image_range[1]]:
        file_path = os.path.join(boxes_directory,file)
        raw = pa.loadim(file_path)
        temp_frames = pa.cropframes(raw,boxes_xy,bx=boxes_width,by=boxes_height)
        
        if boxes_method == 'intensity':
            temp_data = pa.statframes(temp_frames, back = boxes_background)
            listall.append(temp_data[:,0:3])
            
        elif boxes_method == 'centroid':
            temp_data = pa.statframes(temp_frames, back = boxes_background)
            listall.append(temp_data[:,3:8]) 
                
        elif boxes_method == 'gauss':
            temp_data = pa.fitframes(temp_frames, back = boxes_background)
            listall.append(temp_data)    

        elif boxes_method == 'pca':
            temp_data = pa.pcaframes(temp_frames, boxes_meanframe, \
                                     principle_components, back = boxes_background)
            listall.append(temp_data)    
            
        count += 1
        if count == 51:
            print("    ... ",file_path)
            count = 1
            
    # rearrage indices: particle #, image #, data index
    data = np.array(listall).transpose(1,0,2) 
    dims = data.shape
    print("processed {} images using".format(dims[1]),boxes_method)
    print("analyzed {} particles per image".format(dims[0]))

    # create plots
    xlabel = 'image number'
    plot_title = 'track boxes results using ' + boxes_method
    pa.makeplots(data, xlabel=xlabel, ylabel=ylabels[boxes_method], title=plot_title)
 
else:
    print("choose intensity, centroid, gauss or pca.")
        
  