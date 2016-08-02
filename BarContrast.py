import matplotlib.pyplot as plt
import csv
'''This data reads in the output from Aggregator.py, and produces a bar chart showing how frequently a feature appears in the gas map, given that it is present
in the star map.'''
data = list(csv.reader(open('../BETADATA/Aggregation2.csv','r')))

features = ['Regular Rotator', 'Kinematically Distinct Core' ,'Counter-Rotating Core', 'Kinematic Twist', 
            'Double Peak', 'Non-Rotating', 'Disturbed', 'Not Enough Data']
datacount = 0

total = [0,0,0,0,0,0,0,0]
similar = [0,0,0,0,0,0,0,0]
different = [0,0,0,0,0,0,0,0]
y = [0.9125, 0.7925, 0.675, 0.5625, 0.4475, 0.3235, 0.22, 0.099]
fig = plt.figure(1, figsize = (10,10))
fig.suptitle('For galaxies where the gas map shows a feature, how often is that feature present in the star map?', fontsize = 20, y=1.05)
counter = 0
for row in data:
    counter += 1
    if counter > 1: #This stops the code trying to read the header, and can be used to add other conditions (e.g. whether the maps are similar)
        datacount += 1
        stardata = row[3:11]
        gasdata = row[13:21]
        for i in range(8):
            if int(gasdata[i]) > 1:
                total[i] += 1
                if int(stardata[i]) > 1:
                    similar[i] += 1
                else:
                    different[i] += 1
#starts with a list of zeros, and adds one to the relevant element each time a galaxy with that classification is found.
for i in range(8):
    plt.figtext(1, y[i], total[i], fontsize = 18)
#    if total[i] >= 5:
#        colour = '#2171b5'
#    else:
#        colour = '#E62020'
    ax = plt.subplot(8,1,(i+1))
    sim = similar[i]/total[i]
    diff = different[i]/total[i]
    plt.barh((1,2), (diff, sim), color = '#2171b5')
    plt.yticks((1.5,2.5),('Absent', 'Present'), fontsize = 18)
    if i < 7:
        ax.set_xticklabels([])
    plt.title(features[i], fontsize = 18)
    plt.xlim(0,1)
plt.xlabel('Probability', fontsize = 18)

plt.tight_layout(h_pad=0.6)
plt.savefig('../Plots/GasContrastPlot.png', bbox_inches = 'tight')
plt.show()
