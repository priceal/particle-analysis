"""
Performs PCA on set of frames. It will calculate the eigenvector and
singular values as well as the mean peak image.
First 15 eigenimages are displayed and first 20 SVs are plotted.

VARIABLES SET BY SCRIPT:
V          ARRAY OF EIGENVECTORS
S          EIGENVALUES OR SINGULAR VALUES
U          SET OF TRANSFORMATION MATRICES
meanframe      MEAN OF ALL FRAMES

v. 2021 01 27

"""

# define frames to analyze
pca_frames = np.copy(frames)         # input frames, use copy()

## use below to overide parameter values from common.py
######################################################################
pca_background = background    # set to background to use default
pca_normalize = normalize       # set to normalize to use default

############################################################
############################################################
numframes, n, m = pca_frames.shape   

# subtract background value if requested
if pca_background == True:
    for i in range(len(pca_frames)):
        frame = pca_frames[i]
        total = frame.sum(dtype=float)
        borderSum = total - frame[1:-1,1:-1].sum(dtype=float)
        backgroundLevel = borderSum / 2.0 / (n+m-2.0)
        pca_frames[i] = np.clip(frame - backgroundLevel, 0.0, np.Inf)

# normalize (L1) if requested
if pca_normalize == True:
    for i in range(len(pca_frames)):
        total = pca_frames[i].sum(dtype=float)
        pca_frames[i]= pca_frames[i]/total

#pca_data = pca_frames.flatten().reshape(numframes,n*m)        
listall=[] # create an array of all data
for frame in pca_frames:
    listall.append(frame.flatten())
pca_data = np.array(listall)

# now subtract the mean to "center" the data
meanf = pca_data.mean(axis=0)
pca_datac = pca_data - meanf
numpoints = len(pca_datac)
meanframe = meanf.reshape(n,m)

U, S, V = np.linalg.svd(pca_datac) # here we do SVD
print( "processed ", numpoints, "frames.")

fig1, ax = plt.subplots(4,4)
axf = ax.flatten()
axf[0].imshow(meanframe,cmap='gray')
axf[0].set_title('mean' )
axf[0].set_xticks([])
axf[0].set_yticks([])
for i in range(15):
    axf[i+1].imshow(V[i].reshape(n,m),cmap='seismic')
    axf[i+1].set_title('{} ({:.2f})'.format(i,S[i]) )
    axf[i+1].set_xticks([])
    axf[i+1].set_yticks([])

fig2, ax2 = plt.subplots(1,1)
ax2.plot(S[:20],'o')
ax2.set_xlabel('component')
ax2.set_ylabel('singular value')
   
    
    
    
    
    