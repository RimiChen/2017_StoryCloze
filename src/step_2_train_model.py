# This file will output a trained model based on input json
from gensim import models

import sys
import json
import io

json_file = sys.argv[1]

story_sentences = [];
with open(json_file) as json_file:

    json_data = json.load(json_file)
    for e in json_data:
        for k, v in e.items():
            v_noComma = v.replace("," , "")
            result_v = v_noComma.replace("." , "")
            #print(k, "," ,result_v.split(" "))
            v_array = result_v.split(" ");
            if len(v_array) > 1:
            
                temp_sentence = models.doc2vec.LabeledSentence(
                words=result_v.split(" "), tags=[k]
                )
                
                story_sentences.append(temp_sentence)
                #print([result_v.split(" ")])
                
    #print(story_sentences)
    
class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        for uid, line in enumerate(open(filename)):
            yield LabeledSentence(words=line.split(), labels=['SENT_%s' % uid])
            
model = models.Doc2Vec(alpha=.025, min_alpha=.025, min_count=1)
model.build_vocab(story_sentences)

for epoch in range(10):
    model.train( story_sentences)
    model.alpha -= 0.002  # decrease the learning rate`
    model.min_alpha = model.alpha  # fix the learning rate, no decay
    
    
model.save("test_model.doc2vec")
#model_loaded = models.Doc2Vec.load('test_model.doc2vec')

#print(model_loaded.docvecs.similarity("b929f263-1dcd-4a0b-b267-5d5ff2fe65bb_1", "7cbbc0af-bcce-4f56-871d-963f9bb6a99d_1"))

#result =model_loaded.docvecs.most_similar([model_loaded.infer_vector("Mom took us some place special today".split())]) 

#iter = 0 
#for item in result:
#    print(result[iter][0], " with distance: ", result[iter][1])
#    iter = iter + 1