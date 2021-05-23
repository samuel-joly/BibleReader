#coding:utf-8

import os
import re
import numpy as np
import matplotlib.pyplot as plt


word = dict()

for fold in os.listdir('OldTestament'):
	path = 'OldTestament' + '/' + fold

	for content in os.listdir(path):
		txtPath = path + '/' + content

		with open(txtPath, 'r') as file:
			text = file.read()
			text = re.sub(r'\W+',' ', text)
			text = text.split(' ')

			for element in text:
				
				if element in word.keys():
					word[element] = word[element] + 1

				else:
					word[element] = 1

for fold in os.listdir('NewTestament'):
	path = 'NewTestament' + '/' + fold

	for content in os.listdir(path):
		txtPath = path + '/' + content

		with open(txtPath, 'r') as file:
			text = file.read()
			text = re.sub(r'\W+',' ', text)
			text = text.split(' ')

			for element in text:
				if element in word.keys():
					word[element] = word[element] + 1

				else:
					word[element] = 1

alphabet = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,\
			'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,\
			'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

result = [[0] * 26 for _  in np.arange(26)]
 
for element in word.keys():
	element = element.lower()
	for index,char in enumerate(element): 
		if char.isalpha():
			x = alphabet[char]	
			if index+1 < len(element):
				y = alphabet[element[index+1]]
				result[x][y] = result[x][y] + 1

			#if index-1 >= 0:
			#	y = alphabet[element[index-1]]
			#	result[x][y] = result[x][y] +1

			

fig, ax = plt.subplots()
ax.imshow(result, interpolation='nearest')
ax.set_title('Letter Occurence')

x = np.arange(len(result[0]))
plt.xticks(x,alphabet)

y = np.arange(len(result[0]))
plt.yticks(y,alphabet)


plt.show()
