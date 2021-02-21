"""
Analyzes results of tracking and creates plots

v. 2021 02 21
"""

analyze_shape_stats = True
analyze_mobility_stats = True

#############################################################################
#############################################################################

# create plots
print("creating summary dataframes")
trackingMean = trackingGroup.mean()
trackingStd = trackingGroup.std()
plotcols = ["max", "sum" , "<x>", "<y>", "<xx>", "<xy>", "<yy>" ]

print("creating summary plots")
if analyze_shape_stats:
    
    trackingMean[plotcols].hist(bins=50,figsize=(8,7))
    plt.suptitle('particle shape statistics')

    fig, ax = plt.subplots(1,2,figsize=(8,4))
    fig.suptitle('particle shape statistics')
    trackingMean.plot.scatter(x='<xx>',y='<yy>',ax=ax[0])
    trackingMean.plot.scatter(x='sum',y='max',ax=ax[1])
    
if analyze_mobility_stats:
    
    sns.jointplot(data=trackingStd, x='<x>', y='<y>', \
                  marginal_ticks=True, \
                  marginal_kws=dict(bins=50))
    plt.suptitle('particle mobility statistics')
    