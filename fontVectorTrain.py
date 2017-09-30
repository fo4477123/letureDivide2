# -*- coding: utf-8 -*-

from gensim.models import word2vec,TfidfModel
from gensim.models.keyedvectors import KeyedVectors

import logging

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus("wiki_seg.txt")
    #model = word2vec.Word2Vec(sentences, size=250,workers=8)
    

    tfidf = TfidfModel(sentences)
    # Save our model.
    tfidf.save("med250.model2.bin")
    
    print("test")
    
    # To load a model.
    # model = word2vec.Word2Vec.load("your_model.bin")

if __name__ == "__main__":
    main()