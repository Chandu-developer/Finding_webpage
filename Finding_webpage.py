# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 11:31:24 2019

@author: 91779
"""
import urllib.request
import nltk
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/Film')
html = response.read()
#print(html)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
#print(text)

#converting everything into tokens
tokens = [t for t in text.split()]
# print(tokens)

from nltk.corpus import stopwords
from nltk.probability import FreqDist

sr= set(stopwords.words('english'))
clean_tokens = tokens[:]
for token in clean_tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
        
freq = FreqDist(clean_tokens)
#for key,val in freq.items():
  #  print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)