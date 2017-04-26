from gensim import models

import sys
import json
import io
import re
import numpy as np
from scipy import spatial
from random import randint


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
    
    return ans

def get_ending(story):
    result = 0
    reference_stories = []
 
    result_1 = []
    result_2 = []
    
    current_story_id = ""    
    for key, stroy_string in story.items():
        test_index = key.split("_")

        if len(test_index) < 2:
            # the index
            current_story_id = stroy_string
            
        if re.search('((.+?)_\d+$)', key):
            #print(key, ", ", stroy_string)
            number =  re.match('.*?([0-9]+)$', key).group(1)
            #print(number)
            regex = '((.+?)_'+str(number)+'$)'
            ans = get_most_similar(regex,stroy_string)
            #print(ans)
            reference_stories.extend(ans)
        
        
    if len(reference_stories) <= 0:
        #print("\n\nno match story, guess one")
        result = randint(1,2)
        # random between result 1, 2
    else:
    #    print(reference_stories)
        # for each in reference stories check whether the result 1, 2 is closer

        for reference in reference_stories:
            sentence_index = current_story_id+"_5|1"
            target_string = story[sentence_index]
            target_string = target_string.replace(",","")
            target_string = target_string.replace(".","")
            #similar = model.docvecs.similarity(reference+"_5",[model.infer_vector(target_string.split())])
            #print(model.docvecs[reference+"_5"])
            vector_1 = model.docvecs[reference+"_5"]
            vector_2 = model.infer_vector(target_string.split())
            similar = abs(1 - spatial.distance.cosine(vector_1, vector_2))
            result_1.append(similar)
            
            #print("ending 1: ", target_string)
            sentence_index = current_story_id+"_5|2"
            target_string = story[sentence_index]
            target_string = target_string.replace(",","")
            target_string = target_string.replace(".","")
            #similar = model.docvecs.similarity(reference+"_5",reference+"_2")
            vector_1 = model.docvecs[reference+"_5"]
            vector_2 = model.infer_vector(target_string.split())
            similar = abs(1 - spatial.distance.cosine(vector_1, vector_2))
            result_1.append(similar)
            result_2.append(similar)
            #print("ending 2: ", target_string)
            
            
    #print("result 1:")
    #print(result_1)
    #print("result 2:")
    #print(result_2)
    avg_1 = np.mean(result_1)
    avg_2 = np.mean(result_2)
    #print("result 1: ", avg_1, " result 2: ", avg_2)
    
    if avg_1 < avg_2:
        result = 1
    elif avg_1 == avg_2:
        result = randint(1,2)
    else:
        result = 2
        
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
    