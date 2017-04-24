# the purpose of this file is to transform dataset to usable dataset
# read csv file and output a text file with proper format.
# every 100 story, save a file

import csv
import sys
# sys.argv

print("Test subprocess");

def getTrainingSet(csvPath):
    # this function read the training dataset from csv
    # read import csv
    with open(csvPath) as csvfile:
        readCSV = csv.reader(csvfile)
        story_ids = []
        story_titles = []
        story_sen1s = []
        story_sen2s = []
        story_sen3s = []
        story_sen4s = []
        story_sen5s = []

        for row in readCSV:
            story_id = row[0]
            story_title = row[1]
            story_sen1 = row[2]
            story_sen2 = row[3]
            story_sen3 = row[4]
            story_sen4 = row[5]
            story_sen5 = row[6]

            story_ids.append(story_id)
            story_titles.append(story_title)
            story_sen1s.append(story_sen1)
            story_sen2s.append(story_sen2)
            story_sen3s.append(story_sen3)
            story_sen4s.append(story_sen4)
            story_sen5s.append(story_sen5)
            
            
        #print(len(story_ids))
        
        for iter in enumerate(story_ids):
            
#def getTestSet():
    # this function read the test set from csv
    
#print(sys.argv[1])
getTrainingSet(sys.argv[1])
