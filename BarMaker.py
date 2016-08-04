import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
'''This data reads in the output from Aggregator.py, and produces a bar chart showing the frequency of all features.
Please specify the inputfile and outputfile on the command line when running this code'''

data = list(csv.reader(open(str(sys.argv[1]),'r')))

features = ['Regular Rotator', 'Kinematically Distinct Core' ,'Counter-Rotating Core', 'Kinematic Twist', 
            'Double Peak', 'Non-Rotating', 'Disturbed', 'Not Enough Data']
datacount = 0

stars = [0,0,0,0,0,0,0,0]
gas = [0,0,0,0,0,0,0,0]
counter = 0
for row in data:
    counter += 1
    if counter > 1: #This stops the code trying to read the header, and can be used to add other conditions (e.g. whether the maps are similar)
        datacount += 1
        stardata = row[3:11]
        gasdata = row[14:22]
        for i in range(8):
            if int(stardata[i]) > 1:
                stars[i] += 1
            if int(gasdata[i]) > 1:
                gas[i] += 1
#starts with a list of zeros, and adds one to the relevant element each time a galaxy with that classification is found.
        
gas[:] = [x / datacount for x in gas]
stars[:] = [x / datacount for x in stars]
'''divides by the number of galaxies in the sample'''
ind = np.arange(len(gas))*2
height = 0.79
fig = plt.figure(figsize=[20,14])
ax = fig.add_subplot(1,1,1)
plt.barh(ind + height, stars, align='center', color='#2171b5', linewidth = 0, edgecolor = '#00008B', label = 'Stars')
plt.barh(ind, gas, align='center', color='#E62020', linewidth = 0.5, edgecolor = '#FF0000', label = 'Gas')


plt.legend(fontsize = 18)
plt.yticks(ind + height/2, features, fontsize = 18)
plt.xlabel('Probability', fontsize = 18)
ax.set_title('Which of these features are present in the galaxy shown?', fontsize = 23)
plt.xlim(0,1)
plt.savefig(str(sys.argv[2]), bbox_inches = 'tight')
