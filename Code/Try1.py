import nltk
from nltk.tokenize import sent_tokenize,word_tokenize,RegexpTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem.snowball import SnowballStemmer

#Reading Data
data1=open('/home/team3/Data/Unstructed_Data/Inflow/Agro_Income.TXT').read()
data2=open('/home/team3/Data/Unstructed_Data/Inflow/Agro_Income1.TXT').read()
data3=open('/home/team3/Data/Unstructed_Data/Inflow/Agro_Influx.TXT').read()
data4=open('/home/team3/Data/Unstructed_Data/Inflow/Agro_Influx1.TXT').read()
data5=open('/home/team3/Data/Unstructed_Data/Inflow/farmIncome.TXT').read()

#reading data agriculture

data6 = open('/home/team3/Data/Unstructed_Data/agriculture/usAgriculture1.txt').read()
data7 = open('/home/team3/Data/Unstructed_Data/agriculture/usAgriculture2.txt').read()
data8 = open('/home/team3/Data/Unstructed_Data/agriculture/usFarming1.txt').read()
data9 = open('/home/team3/Data/Unstructed_Data/agriculture/usFarming2.txt').read()


#data=data1+data2+data3+data4+data5
data=data1
data_a = data6

#print(data)

#Tokenizing Words
tokenizer=RegexpTokenizer(r'\w+')
w=tokenizer.tokenize(unicode(data,'utf-8'))
stemmer = SnowballStemmer("english")
words=[stemmer.stem(word.lower()) for word in w]
#print(words)
#words=word_tokenize(data)

#print(words)
wordsSelected=[]

#Removing Stopwords
for each_word in words:
    if each_word not in stopwords.words("english"):
        wordsSelected.append(each_word)

#Frequency of words
spread=FreqDist(wordsSelected)
#print(spread.most_common(1000))


########################################################################

#For Dictionary states

import csv
with open('/home/team3/Data/Dictionaries/us_states1.csv','rb') as f:
    reader=csv.reader(f)
    temp=list(reader)
states=[]
[states.append(i[0]) for i in temp]
print(states)

for i in states:
    print(i," ",data.count(i))
#[data.count(i) for i in states]
