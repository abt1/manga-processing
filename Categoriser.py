import csv
import os
'''This code finds the maps of galaxies classified as having particular features and moves them to a different place'''
for f in ['../Sorted/RRs/Marvin.csv','../Sorted/KDCs/Marvin.csv','../Sorted/CRCs/Marvin.csv','../Sorted/KTs/Marvin.csv',
          '../Sorted/DPs/Marvin.csv','../Sorted/NRs/Marvin.csv','../Sorted/DSs/Marvin.csv','../Sorted/NoDataS.csv']:
    with open(f, 'w') as outputfile:
        outputfile.write('Marvin links\n')


data = list(csv.reader(open('../BETADATA/Aggregation2.csv', 'r')))
counter = 0
for row in data:
    counter += 1
    if counter > 1:
        if int(row[3]) > 1:
            os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_stvel_map.png ../Sorted/RRs'.format(row[1],row[2]))
            os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_emvel_map.png ../Sorted/RRs'.format(row[1],row[2]))
            with open('../Sorted/RRs/Marvin.csv', 'a') as outputfile:
                outputfile.write('https://sas.sdss.org/marvin/plate/{0}/{1}/\n'.format(row[1],row[2]))
       
        if int(row[4]) > 1:
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_stvel_map.png ../Sorted/KDCs'.format(row[1],row[2]))
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_emvel_map.png ../Sorted/KDCs'.format(row[1],row[2]))
                with open('../Sorted/KDCs/Marvin.csv', 'a') as outputfile:
                    outputfile.write('https://sas.sdss.org/marvin/plate/{0}/{1}/\n'.format(row[1],row[2]))
        
        if int(row[5]) > 1:
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_stvel_map.png ../Sorted/CRCs'.format(row[1],row[2]))
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_emvel_map.png ../Sorted/CRCs'.format(row[1],row[2]))
                with open('../Sorted/CRCs/Marvin.csv', 'a') as outputfile:
                    outputfile.write('https://sas.sdss.org/marvin/plate/{0}/{1}/\n'.format(row[1],row[2]))
        
        if int(row[6]) > 1:
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_stvel_map.png ../Sorted/KTs'.format(row[1],row[2]))
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_emvel_map.png ../Sorted/KTs'.format(row[1],row[2]))
                with open('../Sorted/KTs/Marvin.csv', 'a') as outputfile:
                    outputfile.write('https://sas.sdss.org/marvin/plate/{0}/{1}/\n'.format(row[1],row[2]))
        
        if int(row[7]) > 1:
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_stvel_map.png ../Sorted/DPs'.format(row[1],row[2]))
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_emvel_map.png ../Sorted/DPs'.format(row[1],row[2]))
                with open('../Sorted/DPs/Marvin.csv', 'a') as outputfile:
                    outputfile.write('https://sas.sdss.org/marvin/plate/{0}/{1}/\n'.format(row[1],row[2]))
        
        if int(row[8]) > 1:
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_stvel_map.png ../Sorted/NRs'.format(row[1],row[2]))
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_emvel_map.png ../Sorted/NRs'.format(row[1],row[2]))
                with open('../Sorted/NRs/Marvin.csv', 'a') as outputfile:
                    outputfile.write('https://sas.sdss.org/marvin/plate/{0}/{1}/\n'.format(row[1],row[2]))
        
        if int(row[9]) > 1:
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_stvel_map.png ../Sorted/DSs'.format(row[1],row[2]))
                os.system('cp ../../Manga_stuff/data/manga-{0}-{1}-LOGCUBE_BIN-NONE-002_emvel_map.png ../Sorted/DSs'.format(row[1],row[2]))
                with open('../Sorted/DSs/Marvin.csv', 'a') as outputfile:
                    outputfile.write('https://sas.sdss.org/marvin/plate/{0}/{1}/\n'.format(row[1],row[2]))
        
        if int(row[10]) > 2:
            with open('../Sorted/NoDataS.csv', 'a') as outputfile:
                outputfile.write('{0},{1}\n'.format(row[1],row[2]))