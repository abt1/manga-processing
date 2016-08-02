import matplotlib.pyplot as plt
import numpy as np
import csv
'''This data reads in the output from Aggregator.py, and produces a bar chart showing the frequency of all features.'''
data = list(csv.reader(open('../Manga_Data_Analysis/FULLDATA/Aggregation.csv','r')))

datacount = 0
results = [0,0,0]
answers = ['Similar', 'Different', 'Misaligned']
for row in data:
    datacount += 1
    if datacount > 1:
        choices = row[11:14]
        for i in range(3):
            if int(choices[i]) > 1:
                results[i] += 1
results[:] = [x/datacount for x in results]
fig = plt.figure(figsize=[20,14])
ax = fig.add_subplot(1,1,1)
plt.barh((1,2,3),results, align='center', color='#2171b5', linewidth = 0, edgecolor = '#00008B')
plt.yticks((1,2,3), answers, fontsize = 18)
plt.xlabel('Probability', fontsize = 18)
ax.set_title('How do the galaxy maps compare?', fontsize = 23)
plt.xlim(0,1)
plt.savefig('../Manga_Data_Analysis/FULLDATA/Plots/YesNoPlot.png', bbox_inches = 'tight')