"""
Analyzes results of tracking and creates plots

v. 2021 02 21
"""
plot_particle = particle0
plotIndex = 1


plot_shape_stats = True
plot_mobility_stats = True

numbins = 120

#############################################################################
#############################################################################
si = str(plotIndex)
plotMeanCols = ["<xx>"+si, "<xy>"+si, "<yy>"+si ]
plotStdCols = ['Sx'+si, 'Sy'+si ]

print("creating summary plots")
if plot_shape_stats:
 
    coordMax = 1.1*max(plot_particle['<xx>'+si].max(), plot_particle['<yy>'+si].max())
    plotStatsShapeG = sns.JointGrid(data=plot_particle, x='<xx>'+si, y='<yy>'+si)
    plotStatsShapeG.plot_joint(sns.scatterplot)
    plotStatsShapeG.plot_marginals(sns.histplot,bins=numbins)
    plotStatsShapeG.ax_joint.set_aspect('equal')
    plotStatsShapeG.ax_joint.set_xlim((0,coordMax))
    plotStatsShapeG.ax_joint.set_ylim((0,coordMax))
    plt.suptitle('particle shape statistics')
    
if plot_mobility_stats:
    
    coordMax = 1.1*max(plot_particle['Sx'+si].max(), plot_particle['Sy'+si].max())
    plotStatsMobG = sns.JointGrid(data=plot_particle, x='Sx'+si, y='Sy'+si)
    plotStatsMobG.plot_joint(sns.scatterplot)
    plotStatsMobG.plot_marginals(sns.histplot,bins=numbins)
    plotStatsMobG.ax_joint.set_aspect('equal')
    plotStatsMobG.ax_joint.set_xlim((-0.03,coordMax))
    plotStatsMobG.ax_joint.set_ylim((-0.03,coordMax))
    plt.suptitle('particle mobility statistics')
    plt.figure()
    sns.histplot(plot_particle['Cxy'+si])
    
    