# get the dependencies
import nltk
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
#read a file

data = open('/gpfs/class/mergedfiles/mergedfile.txt').read()

#create token list

words = word_tokenize(data.decode('latin-1'))

#negative selection, append words to list

wordsSelected = []
for w in words:
	if w not in stopwords.words('english'):
		wordsSelected.append(w)



#stats
spread=FreqDist(words)
print(spread)


# number of words
len(words)

# 100 most common words
spread.most_common(100)

print (wordsSelected) 

