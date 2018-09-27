# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 17:18:00 2018

@author: ME DELL'
"""
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer ,TfidfVectorizer ,TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import pickle 
categories = {
             'comp.os.ms-windows.misc' :'Computers ',
             'rec.autos' :'Autos',
             'rec.motorcycles' : ' Motorcycle',
             'rec.sport.baseball' : 'Baseball',
             'sci.electronics':'Electronics',
             'sci.med':'Medical',
             'sci.space' :'Space',
             'talk.politics.misc':'Politics',
             'talk.religion.misc':'Religion'
            }
            
dataset = fetch_20newsgroups(subset = 'train', categories=categories)
vect = CountVectorizer()
x_train = vect.fit_transform(dataset.data)
tfidf = TfidfTransformer()
x_train = tfidf.fit_transform(x_train)
clf = MultinomialNB()
clf.fit(x_train, dataset.target)
filename = 'finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))