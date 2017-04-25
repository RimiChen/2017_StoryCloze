# the purpose of this file is to transform dataset to usable dataset
# read csv file and output a text file with proper format.
# every 100 story, save a file

import csv
import sys
import json
import io
# sys.argv

#print("Test subprocess");

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

def getTestSet(csvPath, segmentSize):
    # this function read the training dataset from csv
    # read import csv
    with open(csvPath) as csvfile:
        readCSV = csv.reader(csvfile)
        story_ids = []
        story_sen1s = []
        story_sen2s = []
        story_sen3s = []
        story_sen4s = []
        story_sen5_1s = []
        story_sen5_2s = []
        story_answers = []

        for row in readCSV:
            story_id = row[0]
            story_sen1 = row[1]
            story_sen2 = row[2]
            story_sen3 = row[3]
            story_sen4 = row[4]
            story_sen5_1 = row[5]
            story_sen5_2 = row[6]
            story_answer = row[7]

            story_ids.append(story_id)
            story_sen1s.append(story_sen1)
            story_sen2s.append(story_sen2)
            story_sen3s.append(story_sen3)
            story_sen4s.append(story_sen4)
            story_sen5_1s.append(story_sen5_1)
            story_sen5_2s.append(story_sen5_2)
            story_answers.append(story_answer)
            
        #print(len(story_ids))
        storyCount = 0
        currentFileNumber =-1
        currentStories = []
        for iter in enumerate(story_ids):
            #output every 100 lines
            #remove the first row
            tempStroy = {}
            if storyCount == 0:
                #row 0
                print("Remove the first row")
            else:
                #print(story_ids[storyCount])
            
                if storyCount % int(segmentSize) ==1:
                    if len(currentStories)> 0:
                        currentFileNumber = currentFileNumber + 1
                        jsonPath ='../Dataset/testSet/test'+str(currentFileNumber)+'.json'
                        print(jsonPath)

                        with io.open(jsonPath, 'w', encoding='utf8') as outfile:
                            targetString = json.dumps(
                                currentStories,
                                indent=4,
                                separators=(',',': '),
                                ensure_ascii=False
                            )
                            outfile.write(to_unicode(targetString))
                        outfile.close()

                    currentStories = []
                tempStroy[str(storyCount)] = story_ids[storyCount];       
                tempStroy[story_ids[storyCount]+'_1'] = (story_sen1s[storyCount])
                tempStroy[story_ids[storyCount]+'_2'] = (story_sen2s[storyCount])
                tempStroy[story_ids[storyCount]+'_3'] = (story_sen3s[storyCount])
                tempStroy[story_ids[storyCount]+'_4'] =(story_sen4s[storyCount])
                tempStroy[story_ids[storyCount]+'_5|1'] =(story_sen5_1s[storyCount])
                tempStroy[story_ids[storyCount]+'_5|2'] =(story_sen5_2s[storyCount])
                tempStroy[story_ids[storyCount]+'_ans'] =(story_answers[storyCount])
                
                currentStories.append(tempStroy)

            storyCount = storyCount + 1
            


def getAnswerSet(csvPath, segmentSize):
    # this function read the training dataset from csv
    # read import csv
    with open(csvPath) as csvfile:
        readCSV = csv.reader(csvfile)
        story_ids = []
        story_answers = []

        for row in readCSV:
            story_id = row[0]
            story_answer = row[7]

            story_ids.append(story_id)
            story_answers.append(story_answer)
            
        #print(len(story_ids))
        storyCount = 0
        currentFileNumber =-1
        currentStories = []
        for iter in enumerate(story_ids):
            #output every 100 lines
            #remove the first row
            tempStroy = {}
            if storyCount == 0:
                #row 0
                print("Remove the first row")
            else:
                #print(story_ids[storyCount])
            
                if storyCount % int(segmentSize) ==1:
                    if len(currentStories)> 0:
                        currentFileNumber = currentFileNumber + 1
                        jsonPath ='../Dataset/testSet/answer'+str(currentFileNumber)+'.json'
                        print(jsonPath)

                        with io.open(jsonPath, 'w', encoding='utf8') as outfile:
                            targetString = json.dumps(
                                currentStories,
                                indent=4,
                                separators=(',',': '),
                                ensure_ascii=False
                            )
                            outfile.write(to_unicode(targetString))
                        outfile.close()

                    currentStories = []
                #tempStroy[str(storyCount)] = story_ids[storyCount];       
                tempStroy[story_ids[storyCount]] =(story_answers[storyCount])
                
                currentStories.append(tempStroy)

            storyCount = storyCount + 1
            
            
            #whenever processing a story, storyCount +1
#def getTestSet():
    # this function read the test set from csv
    
#print(sys.argv[1])
getTestSet(sys.argv[1], sys.argv[2])
getAnswerSet(sys.argv[1], sys.argv[2])
