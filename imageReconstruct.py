"""
calculates image reconstrucion of a frame using PCA results. Must run pca.py
on your frames first. Set recon_particle to the particle df and choose
which particle with recon_particle_number. Set recon_image to the
image you used for pca.py.

"""
# set particle dataframe and particle number to resconstruct. also set image to use
recon_particle = particle0
recon_particle_number = 88
recon_image = 0

# if pca method is chosen, must define pca principle components here
recon_components =  [ V[0], V[1], V[2], V[3], V[4], V[5], V[6]]

recon_cmap = 'gray'
recon_clip = True

## use below to overide parameter values from common.py
######################################################################
recon_meanframe = meanframe   # this should not need to be changed
recon_width = buffer_width              
recon_height = buffer_height
recon_background = background   # set to background to use default
recon_normalize = normalize       # set to normalize to use default

# do not change code below this line
############################################################
############################################################

# load in the frames
recon_frames = pa.cropframes(recon_image, recon_particle, bx = recon_width, \
                                     by = recon_height, imgDF = imageDF)

# subtract background if requested
#if recon_background == True:
#    recon_frame = pa.background_single(recon_frames[recon_particle_number]) 
#else:
#    recon_frame = recon_frames[recon_particle_number]

recon_frame = recon_frames[recon_particle_number]
numFrames,n, m = recon_frames.shape   
data = pa.pcaframe(recon_frame, recon_meanframe, \
                            recon_components, back = recon_background )

expansion = np.broadcast_to(data,(n*m,len(data))).T * np.array(recon_components)
reconstruction = recon_meanframe + expansion.sum(axis=0).reshape((n,m))
recon_frame_back = pa.background_single(recon_frame)

figr, axr = plt.subplots(1,len(recon_components)+3 )

axr[0].set_title('original' )
axr[0].set_xticks([])
axr[0].set_yticks([])
#axr[0].imshow(recon_frame,cmap='gray')
axr[0].imshow(recon_frame_back, norm=TwoSlopeNorm(vcenter=0), \
                    cmap=recon_cmap, interpolation='none')    

axr[1].set_title('mean' )
axr[1].set_xticks([])
axr[1].set_yticks([])
#axr[1].imshow(recon_meanframe,cmap='gray')
axr[1].imshow(recon_meanframe, norm=TwoSlopeNorm(vcenter=0), \
                    cmap=recon_cmap, interpolation='none')    

for i in range(len(recon_components)):
    axr[i+2].imshow(V[i].reshape(n,m), norm=TwoSlopeNorm(vcenter=0), \
                    cmap='seismic', interpolation='none')    
    axr[i+2].set_title('{} ({:3.1f})'.format(i,data[i]) ) 
    axr[i+2].set_xticks([])
    axr[i+2].set_yticks([])
    
if recon_clip:
    reconstruction = np.clip(reconstruction,0,np.Inf)    
axr[len(recon_components)+2].set_title('recon' )
axr[len(recon_components)+2].set_xticks([])
axr[len(recon_components)+2].set_yticks([])
axr[len(recon_components)+2].imshow(reconstruction,cmap='gray')
axr[len(recon_components)+2].imshow(reconstruction, norm=TwoSlopeNorm(vcenter=0), \
                    cmap=recon_cmap, interpolation='none')    
    