# -*- coding: utf-8 -*-
"""
does a set subtraction, removing one set of particles from another. The 
resulting particles are returned in a new particle dataframe called particleR.

The set subtraction is

particleR = all_particles - remove_particles

You can then use this particle dataframe (particleR) in trackParticles

v. 2021 03 10
"""

all_particles = particle0  # the particle dataframe to subtract FROM
remove_particles = particle100  # the particle dataframe that will be subtracted


#############################################################################
remove_bx = buffer_width
remove_by = buffer_width        
#############################################################################
#############################################################################

xy0 = all_particles[['x','y']].to_numpy()
xy1 = remove_particles[['x','y']].to_numpy()
xyS = pa.subtractxy(xy0,xy1,bx=remove_bx,by=remove_by)     
particleR =  pd.DataFrame( data=xyS, columns=['x','y'])


