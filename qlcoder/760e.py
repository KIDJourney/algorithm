train = []
target = []

f = open('adult.txt')

tags = f.readline()
tags = tags.strip().split(',')
lines = f.readlines()

for line in lines :
    line = line.strip().split(',')
    data = {}
    for index , tag in enumerate(tags[:-1]):
        data[tag] = line[index]
    train.append(data)
    target.append(line[-1])

from sklearn.feature_extraction import DictVectorizer
import numpy as np

vec = DictVectorizer()

train = vec.fit_transform(train).toarray()
target = np.array(target)

from sklearn.svm import SVC

clf = SVC()
clf.fit(tarin , target)

pred = []
pred_lines = open('adult_test.txt').readlines()

for line in pred_lines :
    data = {}
    line = line.strip().split(',')
    for index , tag in enumerate(tags[:-1]):
        data[tag] = line[index]
    pred.append(data)

pred = vec.fit_transform(pred).toarray()

clf.predict(pred)
