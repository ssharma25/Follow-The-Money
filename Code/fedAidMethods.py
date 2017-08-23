import nltk
from nltk.tokenize import sent_tokenize,word_tokenize,RegexpTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem.snowball import SnowballStemmer
import csv
import psycopg2

#read data
def read_file(filepath):
	return open(filepath).read()

def splitLexisNexis(filepath, startNum, endNum):
	i = startNum + 1;
	regex = str(i) + ' of ' + str(endNum) + ' DOCUMENTS'
	
	articles = []
	currentArticle = ''
	current = 0
	
	with open(filepath) as infile:
		for line in infile:
			if regex not in line:
				currentArticle += line
			else:
				items = line.split(regex)
				currentArticle += items[0]
				articles.append(currentArticle)
				current = current + 1
				currentArticle = items[1]
				i = i + 1
				regex = str(i) + ' of ' + str(endNum) + ' DOCUMENTS'
				
	return articles
	
#tokenize and stem
def tokenize_stem_file(data):
	tokenizer=RegexpTokenizer(r'\w+')
	w=tokenizer.tokenize(unicode(data,'utf-8'))
	stemmer = SnowballStemmer("english")
	words=[stemmer.stem(word.lower()) for word in w]
	return words
	
#stopwords
def remove_stopWords(words):
	wordsSelected=[]

	for each_word in words:
		if each_word not in stopwords.words("english"):
			wordsSelected.append(each_word)
	return wordsSelected

#frequency
def get_frequency(wordsSelected):
	return FreqDist(wordsSelected)
	
#import dictionaries
def read_csvDictionary(filepath):
	with open(filepath,'rb') as f:
		reader=csv.reader(f)
		temp=list(reader)
	_dict = []
	[_dict.append(i[0]) for i in temp]
	return _dict
	#print(_dict)
	
#word count
#Pass i for case insensitive
def word_count(_dict, doc, case='n'):
	word_count_dict = {}
	if case=='i':
                doc=doc.lower()
        elif case=='n':
                pass
        for i in _dict:
                word_count_dict[i] = doc.count(i)    
	return word_count_dict

def dict_sum1(word_count_dict):
	return sum(word_count_dict.values())
	
#counting words
def dict_sum(_dict, doc, case='n'):
	sum = 0
	if case=='i':
                doc=doc.lower()
        elif case=='n':
                pass
	for i in _dict:
		sum = sum + doc.count(i)
	#[data.count(i) for i in _dict]
	return sum
#database
def db(doc_name, dict1, dict2, dict3, dict4):
	sums = dict1 + dict2 + dict3 + dict4
	conn = psycopg2.connect("dbname='team3' user='team3' host='localhost' password='Toowie3a'")
	cur = conn.cursor()
	query = "Insert into ftm.truthtable values (%s,%s,%s,%s,%s,%s)"
	data = (doc_name, dict1, dict2, dict3, dict4, sums)
	cur.execute(query, data)
	conn.commit()
	conn.close()
	
def articleDb(doc_name, dict1, dict2, dict3, dict4):
	sums = dict1 + dict2 + dict3 + dict4
	conn = psycopg2.connect("dbname='team3' user='team3' host='localhost' password='Toowie3a'")
	cur = conn.cursor()
	query = "Insert into ftm.truthtable_by_article values (%s,%s,%s,%s,%s,%s)"
	data = (doc_name, dict1, dict2, dict3, dict4, sums)
	cur.execute(query, data)
	conn.commit()
	conn.close()

def fedAidDb(doc_name, dict1, dict2, dict3, dict4):
	sums = dict1 + dict2 + dict3 + dict4
	conn = psycopg2.connect("dbname='team3' user='team3' host='localhost' password='Toowie3a'")
	cur = conn.cursor()
	query = "Insert into ftm.fedAidDb values (%s,%s,%s,%s,%s,%s)"
	data = (doc_name, dict1, dict2, dict3, dict4, sums)
	cur.execute(query, data)
	conn.commit()
	conn.close()
	
	
	
	
