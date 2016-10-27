import json
from pprint import pprint

textdata = []
rownum = 1
with open('pokemon.json') as data_file: 
	for line in data_file: 
		if((rownum % 2) == 1):
	    		data = json.loads(line)
			textdata.append(data['text'])
		rownum += 1
print(textdata)

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

allwords=[]
tokenizer = RegexpTokenizer(r'\w+')
for num in range(len(textdata)):
	raw = textdata[num].lower()
	tokens = tokenizer.tokenize(raw)
	en_stop = get_stop_words('en')
	stopped_tokens = [i for i in tokens if (len(i)>5 and len(i)<20 and not i in en_stop)]
	allwords.append(stopped_tokens)

print(allwords)

import itertools
newAllwords = list(itertools.chain.from_iterable(allwords))
print(newAllwords)

totaldict = sorted(set(newAllwords))
print(totaldict)

from collections import Counter
aa = Counter(newAllwords)    #aa is a dictionary{"word": num}
print aa


