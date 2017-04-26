from gensim import models

import sys
import json
import io
import re
import numpy as np
from scipy import spatial
from random import randint
#from itertools import izip 


try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# get trained model
model = models.Doc2Vec.load(sys.argv[1])
#print(model['9a51198e-96f1-42c3-b09d-a3e1e067d803_5'])
# define check function
def get_most_similar(regex, target):
    target = target.replace(",", "")
    target = target.replace(".", "")
    #print(target)
    result_story_id = model.docvecs.most_similar([model.infer_vector(target.split())])

    # process result array
    
    iter = 0
    ans = []
    currentMin = 10
    currentMinStory = ""
    for item in result_story_id:
        text = result_story_id[iter][0]
        match = re.search(regex, text)
        check_index = text.split("_")
        if match and len(check_index) == 2:
            match_story = re.sub('_\d+$', '',result_story_id[iter][0])
            ans.append(match_story)
            
            #print("\n##", len(check_index))
            #print(
            #"story ",
            #match_story,
            #" label: ",result_story_id[iter][0],
            #" with distance: ", result_story_id[iter][1]
            #)
        #else:
        #    print("not match")
        iter = iter + 1
    
    ans.append(currentMinStory)
    
    return ans

def get_ending(story):
    result = randint(1,2)
      
    return result
    
json_file = sys.argv[2]
# read test set
final_answer = []
answerSet = {}
with open(json_file) as json_file:
    testSet = json.load(json_file)
    for e in testSet:
        #each story
        #print(e)
        currentStory = {}
        current_index = "";
        answerSet = {}
        for k, v in e.items():
            test_key = k.split("_")
            if len(test_key) < 2:
                current_index = v
            currentStory[k] = v;
        
        #print(currentStory)
        result_ending = get_ending(currentStory)
        answerSet[current_index] = str(result_ending)
        final_answer.append(answerSet)
        
        #print(current_index, " ending: ",result_ending)
    #print(story_sentences)
        

#print(answerSet)
jsonPath = sys.argv[3]
with io.open(jsonPath, 'w', encoding='utf8') as outfile:
    targetString = json.dumps(
    final_answer,
    indent=4,
    separators=(',',': '),
    ensure_ascii=False
    )
    outfile.write(to_unicode(targetString))
    outfile.close()        
#result = model.docvecs.most_similar([model.infer_vector("Mom took us some place special today".split())]) 

#iter = 0 
#for item in result:
#    text = result[iter][0]

#    match = re.search('((.+?)_1)', text)
#    if match:
#        match_story = re.sub('_\d+$', '',result[iter][0])
#        print("story ", match_story, " label: ",result[iter][0], " with distance: ", result[iter][1])

#    iter = iter + 1
    