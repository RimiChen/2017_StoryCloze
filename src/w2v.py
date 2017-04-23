# Explore Google's huge Word2Vec model.

from gensim.models import word2vec
import gensim
import logging

print(word2vec.FAST_VERSION)
# Logging code taken from http://rare-technologies.com/word2vec-tutorial/
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Load Google's pre-trained Word2Vec model.
#model =  gensim.models.KeyedVectors.load_word2vec_format('../Models/GoogleNews-vectors-negative300.bin', binary=True)

#test = model['computer'];
#print(test)