# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 08:38:08 2021

@author: priceal
"""

image_number = 0

# set parameters for particle filtering
sigma = 2.0 # smoothing HWHH
dims = (11,11) # window size for particle filter kernel
norm = 3.0    # normalization for +kernal portion

##############################################################################
##############################################################################

image = pa.loadim( imageDF['path'][image_number] )

#imageGauss = cv.GaussianBlur(image,dims,sigma)
imageFiltered = pa.particleFilter(image,sigma,dims,norm=norm)

#fig, ax = plt.subplots(1,3,sharex='row',sharey='row')
fig, ax = plt.subplots(1,2,sharex='row',sharey='row')

ax[0].imshow(image,cmap='gray',interpolation='nearest')
ax[0].set_title('image')

#ax[1].imshow(imageGauss, cmap='gray',interpolation='nearest')
#ax[1].set_title('Gaussian blur')

ax[1].imshow(imageFiltered,cmap='gray',interpolation='nearest')
ax[1].set_title('particle filter')

#ax[3].imshow(temp3,cmap='gray',interpolation='nearest')
#ax[3].set_title('image 3')
plt.show()
