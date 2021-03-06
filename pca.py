"""
Performs PCA on set of frames. The frames are defined by the particle df and
the image used. Using the pca_width and pca_height, frames centered on the 
particle coordinates are cropped from the image. Then it will calculate the 
eigenvectors and singular values as well as the mean frame.
First 15 eigenimages are displayed and first 20 SVs are plotted.

VARIABLES SET BY SCRIPT:
V          ARRAY OF EIGENVECTORS
S          EIGENVALUES OR SINGULAR VALUES
U          SET OF TRANSFORMATION MATRICES
meanframe      MEAN OF ALL FRAMES

v. 2021 03 11

"""
# define frames to analyze
pca_particle = particle0         # particle dataframe
pca_image = 0                    # image to use

## use below to overide parameter values from common.py
######################################################################
pca_width = buffer_width
pca_height = buffer_height
pca_background = background    # set to background to use default
pca_normalize = normalize       # set to normalize to use default

############################################################
############################################################

# load in the frames
pca_frames = pa.cropframes(pca_image, pca_particle, bx = pca_width, \
                                     by = pca_height, imgDF = imageDF)

numframes, n, m = pca_frames.shape   

listall=[] # create an array of all data
# subtract background value if requested
if pca_background == True:
    for frame in pca_frames:
        listall.append( pa.background_single(frame).flatten() )
else:
    for frame in pca_frames:
        listall.append(frame.flatten())
        
#pca_data = pca_frames.flatten().reshape(numframes,n*m)        
pca_data = np.array(listall)

# now subtract the mean to "center" the data
meanf = pca_data.mean(axis=0)
pca_datac = pca_data - meanf
numpoints = len(pca_datac)
meanframe = meanf.reshape(n,m)

U, S, V = np.linalg.svd(pca_datac) # here we do SVD
print( "processed ", numpoints, "frames.")

fig1, ax = plt.subplots(4,4, figsize = (5,6))
axf = ax.flatten()
axf[0].imshow(meanframe,cmap='gray')
axf[0].set_title('mean' )
axf[0].set_xticks([])
axf[0].set_yticks([])
for i in range(15):
    axf[i+1].imshow(V[i].reshape(n,m), norm=TwoSlopeNorm(vcenter=0), \
                    cmap='seismic', interpolation='none')    
    axf[i+1].set_title('{} ({:.2f})'.format(i,S[i]) )
    axf[i+1].set_xticks([])
    axf[i+1].set_yticks([])

fig2, ax2 = plt.subplots(1,1)
ax2.plot(S[:20],'o')
ax2.set_xlabel('component')
ax2.set_ylabel('singular value')
   
    
    
    
    
    