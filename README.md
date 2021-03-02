# particle-analysis
Tools for analyzing images of particles. Intended for use analyzing images of small, isolated reasonably behaved particles whose 
motion is contained in a small patch surrounding the mean position. E.g., tethered particle motion or bead loss assays.

There are two main dataframes produced.

1. The particle df, which is produced by the findParticles script and which contains 3 required series:
    1) a unique index for each particle
    2) the (x,y) coordinates in pixels of the central pixel
    3) the intensity of the central pixel

It also can contain additional optional series added as analysis is performed on the particles:
    4) the dwell time of the particle (image # where it disappears)
    5) statistics on the particle --- the statistics can contain info on particle shape and/or dynamics

2. The tracking df, which is produced by the trackParticles script.
    "particle" : the particle index from the particle df
    "image" : the image number where the subsequent data was calculated
    "max" : max intensity in the patch containing the particle
    "min" : min intensity in the patch
    "sum" : sum of all intensities in patch
    "<x>" : x-coord of centroid
    "<y>" : y-coord on centroid
    "<xx>" : second moments
    "<xy>" : etc.
    "<yy>" : etc.

