"""
Analyzes results of tracking and creates plots

v. 2021 02 21
"""

analyze_shape_stats = True
analyze_mobility_stats = True


analyzeGroup = addStatsGroup


numbins = 80

#############################################################################
#############################################################################

# create plots
print("creating summary dataframes")
trackingMean = analyzeGroup.mean()
trackingStd = analyzeGroup.std()
plotcols = ["max", "sum" , "<x>", "<y>", "<xx>", "<xy>", "<yy>" ]

print("creating summary plots")
if analyze_shape_stats:
    
    trackingMean[plotcols].hist(bins=numbins,figsize=(8,7))
    plt.suptitle('mean particle statistics')

#    fig, ax = plt.subplots(1,2,figsize=(8,4))
#    fig.suptitle('particle shape statistics')
#    trackingMean.plot.scatter(x='<xx>',y='<yy>',ax=ax[0])
#    trackingMean.plot.scatter(x='sum',y='max',ax=ax[1])
    
    sns.jointplot(data=trackingMean, x='<xx>', y='<yy>', \
                  marginal_kws=dict(bins=numbins))
    plt.suptitle('particle shape statistics')
    
    sns.jointplot(data=trackingMean, x='sum', y='max', \
                  marginal_kws=dict(bins=numbins))
    plt.suptitle('particle intensity statistics')
    
    
if analyze_mobility_stats:
    
    sns.jointplot(data=trackingStd, x='<x>', y='<y>', \
                  marginal_kws=dict(bins=numbins))
    plt.suptitle('particle mobility statistics')
    