# Use this after analyzetracks to remove points that have sigma values below
# a cutoff
# after running analyze tracks, x and y will hold sigmax and sigma y values
# this will screen those and create new xy and data arrays that keep
# only the data points w/ sigma values above the cutoff

# VARIABLES NEEDED BY SCRIPT
# x, y, xy and data

# VARIABLE SET BY SCRIPT:
# xykeep     the array of coords of peaks kept
# datakeep   the data array for the remaining peaks, after running this
#            go back to analyzetracks and replace 'data' with 'datakeep'
#            and re-run
    




# the cutoffs for sigmax and sigmay
minimum_sigmax = 0.0025
minimum_sigmay = 0.0025


#################################################################
xa = list( np.argwhere( x > minimum_sigmax )[:,0] )
ya = list( np.argwhere( y > minimum_sigmay )[:,0] )

keepset = set(xa) | set(ya)
keeplist = list(keepset)
keeplist.sort()

xykeep = pa.selectxy( xy, keeplist )
datakeep = pa.selectxy( data, keeplist )