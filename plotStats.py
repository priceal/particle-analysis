"""
Analyzes results of tracking and creates plots

v. 2021 02 21
"""
plot_particle = particle0
plotIndex = 2

plot_shape_stats = False
plot_mobility_stats = True

numbins = 80

#############################################################################
#############################################################################

si = str(plotIndex)
plotMeanCols = ["<xx>"+si, "<xy>"+si, "<yy>"+si ]
plotStdCols = ['s<x>'+si, 's<y>'+si]

print("creating summary plots")
if plot_shape_stats:
    
#    plot_particle[plotMeanCols].hist(bins=numbins)
#    plt.suptitle('mean particle statistics')
    
    sns.jointplot(data=plot_particle, x='<xx>'+si, y='<yy>'+si, \
                  marginal_kws=dict(bins=numbins))
    plt.suptitle('particle shape statistics')
    
if plot_mobility_stats:
    
    sns.jointplot(data=plot_particle, x='s<x>'+si, y='s<y>'+si, \
                  marginal_kws=dict(bins=numbins))
    plt.suptitle('particle mobility statistics')
    