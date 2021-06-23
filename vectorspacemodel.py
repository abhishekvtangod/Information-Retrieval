# -*- coding: utf-8 -*-
"""VectorSpaceModel.ipynb

Automatically generated by Colaboratory.

"""

# for each text file, we will open it,read all contents, tokenize, remove stop words, perform stemming and lastly count vectorization

# lets hope my laptop does not burn
import os
import nltk
import re
txtlist = []
print(os.getcwd())
# os.chdir("PreProcess")
for filename in os.listdir("."):
    with open(filename, encoding='utf8', errors="ignore") as f:
        contents = f.read()
        # print(type(contents))
        # contents.decode('utf-8')
        contents.replace('\n', ' ')
        contents.replace('\r', ' ')
        txtlist.append(contents)

"""# Question 1 Text Preprocessing"""

# removing punctuation
import string
def rem_punc(text):
    new_text = "".join(char for char in text if char not in string.punctuation)
    return new_text

for i in range(len(txtlist)):
    txtlist[i] = rem_punc(txtlist[i])

# tokenization
for i in range(len(txtlist)):
    l = re.split('\W+',txtlist[i])
    for j in range(len(l)):
        l[j] = l[j].lower()
    txtlist[i] = l

# removing stop words
import nltk
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

for i in range(len(txtlist)):
    x = list(filter(lambda x: x not in stopwords,txtlist[i]))
    txtlist[i] = x

# lemmatizing
nltk.download("wordnet")

wnl = nltk.WordNetLemmatizer()
for i in range(len(txtlist)):
    for j in range(len(txtlist[i])):
        txtlist[i][j] = wnl.lemmatize(txtlist[i][j])
    txtlist[i] = list(set(txtlist[i]))
    
# print(txtlist[0])

# converting lemmatized list to string. not sure why but count vectorization needs string not list

for i in range(len(txtlist)):
    x = ""
    for y in txtlist[i]:
        x = x+" "+y
    txtlist[i] = x

queries = [
    "venus earth mars jupiter",
    "biology cell animal hutchinson evolution",
    "meteor comet nebular theory nebula comet theory",
    "naturalist",
    "xyz pqr"
]

"""# Vector Space Model"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
cvec = TfidfVectorizer(analyzer='word')
x_counts = cvec.fit_transform(txtlist + queries)
# print(x_counts)
vec_dataset = pd.DataFrame(x_counts.toarray())
vec_dataset

from functools import reduce
def mag(x):
    s = 0
    for i in x:
        s += i*i
    return s**0.5

def dot_product(x, y):
    numer = 0
    #print("entered dot product function")
    for i in range(len(x)):
        numer += x[i]*y[i]
    #print("done with numerator")
    denom = mag(x)*mag(y)
    return numer/denom
    
vec_list = vec_dataset.values.tolist()
cosine_similarity = []
for i in range(4, 9):
    for j in range(0, 4):
        #print("Iteration {} {}".format(i, j))
        cosine_similarity.append(dot_product(vec_list[i], vec_list[j]))
    print("cosine similarities for query {}".format(i-4))
    print(cosine_similarity)
    print("Highest Ranked Document: {}".format(cosine_similarity.index(max(cosine_similarity))))
    print("--------------------------------")
    cosine_similarity = []

os.chdir("..")

with open("preprocessed_text", "w") as f:
    for ele in txtlist:
        f.write(ele+'\n')

