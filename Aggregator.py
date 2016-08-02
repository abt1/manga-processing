import csv
import json

'''This code reads in the raw classification data downloaded from the
    Zooniverse and converts it to a human-friendly csv.
It has not been written to include the new option for 'misaligned' galaxies.'''

inputfile = list(csv.reader(open('../BETADATA/RawClassifications.csv', 'r')))
outputfile = open('../BETADATA/Aggregation2.csv', 'w')

outputfile.write("Subject ID, PLATE, IFUDSGN, Regular Rotation,Kinematically Distinct Core, Counter-Rotating Core,"
                 "Kinematic Twist,Double Peak, Non-Rotating, Disturbed, Not enough data present/ can't tell, Similar, Different,"
                 "Regular Rotation,Kinematically Distinct Core, Counter-Rotating Core,Kinematic Twist,Double Peak,"
                 "Non-Rotating, Disturbed, Not enough data present/ can't tell/ No gas detected, Username,"
                 "Number of Classifications, MaNGA-ID\n")
outputfile.close()
Columnslist = ['PLATE', 'IFUDSGN', 'Regular Rotation', 'Kinematically Distinct Core', 'Counter-Rotating Core',
               'Kinematic Twist', 'Double Peak', 'Non-Rotating', 'Disturbed', "Not enough data present/can't tell",
               'Similar', 'Different', 'Regular RotationG', 'Kinematically Distinct CoreG', 'Counter-Rotating CoreG',
               'Kinematic TwistG', 'Double PeakG', 'Non-RotatingG', 'DisturbedG', "Not enough data present/can't tell/ No gas detectedG",
               'Username', 'Classifications', 'MaNGA-ID']

omnidict = {}
for row in inputfile:
    if row[6] == '39.157':
        featurelist = ['Regular Rotation', 'Kinematically Distinct Core',
                       'Counter-Rotating Core', 'Kinematic Twist', 'Double Peak', 'Non-Rotating',
                       'Disturbed', "Not enough data present/can't tell", 'Similar', 'Different']
        featurelist2 = ['Regular RotationG', 'Kinematically Distinct CoreG',
                        'Counter-Rotating CoreG', 'Kinematic TwistG', 'Double PeakG', 'Non-RotatingG',
                        'DisturbedG', "Not enough data present/can't tell/ No gas detectedG"]
        featuredict = {'Regular Rotation': 0, 'Kinematically Distinct Core': 0,
                       'Counter-Rotating Core': 0, 'Kinematic Twist': 0, 'Double Peak': 0, 'Non-Rotating': 0,
                       'Disturbed': 0, "Not enough data present/can't tell": 0, 'Similar': 0, 'Different': 0}
        featuredict2 = {'Regular RotationG': 0, 'Kinematically Distinct CoreG': 0,
                        'Counter-Rotating CoreG': 0, 'Kinematic TwistG': 0, 'Double PeakG': 0, 'Non-RotatingG': 0,
                        'DisturbedG': 0, "Not enough data present/can't tell/ No gas detectedG": 0}
        metadata = json.loads(row[12])
        classification = json.loads(row[11])   #answers
        answer1 = classification[0]['value']   #answer to q1
        answer2 = classification[1]['value']   #answer to q2
        for a in answer1:
            featuredict[a] += 1   #makes the dictionary a binary representation of the classification
        if answer2 == 'Yes':
            featuredict['Similar'] += 1
            for a in answer1:
                if a != "Not enough data present/can't tell":
                    featuredict2[a + 'G'] += 1
                else:
                    featuredict2["Not enough data present/can't tell/ No gas detectedG"] += 1
        if answer2 == 'No':
            featuredict['Different'] += 1
            answer3 = classification[2]['value']
            for a in answer3:
                featuredict2[a + 'G'] += 1
        subjectdata = {'PLATE': metadata[list(metadata.keys())[0]]['PLATE'],
                       'IFUDSGN': metadata[list(metadata.keys())[0]]['IFUDSGN'],
                       'Similar?': answer2, 'Username': row[1], 'Classifications': 1,
                       'MaNGA-ID': metadata[list(metadata.keys())[0]]['MaNGA-ID']}
        data = {**subjectdata, **featuredict, **featuredict2}          #makes one dictionary containing metadata and classifications

        ID = list(metadata.keys())[0]

        if ID in omnidict:
            if data['Username'] not in omnidict[ID]['Username']:   #checks whether the subject has a previous classification
                for f in featurelist:
                    omnidict[ID][f] += data[f]
                for f in featurelist2:
                    omnidict[ID][f] += data[f]
                omnidict[ID]['Username'] += ' ' + data['Username']
                omnidict[ID]['Classifications'] += data['Classifications']
        else:
            omnidict[ID] = data

outputfile = open('../BETADATA/Aggregation2.csv', 'a')
for i in omnidict:
    if omnidict[i]['Classifications'] > 2:
        line = ('{0},'.format(i))
        for c in Columnslist:
            line += ('{0},'.format(omnidict[i][c]))
        line = line[:-1]
        line += ('\n')
        outputfile.write(line)   #saves the nice data as a csv. To change the order of the columns, change the write statement and 'columnslist' at the top of the page

outputfile.close()
