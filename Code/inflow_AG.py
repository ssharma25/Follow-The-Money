from common_methodsArticles import read_file, tokenize_stem_file, remove_stopWords, get_frequency, read_csvDictionary, dict_sum, db, splitLexisNexis, articleDb
import re

def read_data(fp, start, end, docname):
	articles = splitLexisNexis(fp, start, end)
	i = start
	for currentArticle in articles:
		#tokenize
		#words1 = tokenize_stem_file(currentArticle)
		#words2 = tokenize_stem_file(doc2)
		
		#words1 = remove_stopWords(words1)
		#words2 = remove_stopWords(words2)
		#freq1 = get_frequency(words1)
		#freq2 = get_frequency(words2)
		
		dict1 = read_csvDictionary('/home/team3/Data/Dictionaries/us_states1.csv')
		dict2 = read_csvDictionary('/home/team3/Data/Dictionaries/us_states_shortname.csv')
		dict3 = read_csvDictionary('/home/team3/Data/Dictionaries/inflow.csv')
		dict4 = read_csvDictionary('/home/team3/Data/Dictionaries/agriculture.csv')

                state_full=""
                for state in dict1:
                    if currentArticle.count(state)>0:
                        state_full=state
                """for state in dict2:
                    if currentArticle.count(state)>0:
                        state_short=state"""
                if state_full!="" and dict_sum(dict3,currentArticle)>0 and dict_sum(dict4,currentArticle)>0:
                    m=re.search('\-?\$?(?:(?:\d{1,3}(?:,+\d{3}){1,})|\d{4,})\.\d{2}',currentArticle)
                    print(m.group(0))
		#for doc1
		"""dict_sum11 = dict_sum(dict1, currentArticle)
		dict_sum12 = dict_sum(dict2, currentArticle,'i')
		dict_sum13 = dict_sum(dict3, currentArticle,'i')
		dict_sum14 = dict_sum(dict4, currentArticle,'i')
		"""
		#for doc2
		#dict_sum21 = dict_sum(dict1, doc2)
		#dict_sum22 = dict_sum(dict2, doc2,'i')
		#dict_sum23 = dict_sum(dict3, doc2,'i')
		#dict_sum24 = dict_sum(dict4, doc2,'i')
		
		#print("    ","dict1","dict2","dict3","dict4")
		#print("Doc1",dict_sum11,dict_sum12,dict_sum13,dict_sum14)
		#print("Doc2",dict_sum21,dict_sum22,dict_sum23,dict_sum24)
		
		#print(docname + str(i), dict_sum11,dict_sum12,dict_sum13,dict_sum14)
		#articleDb(docname + str(i), dict_sum11,dict_sum12,dict_sum13,dict_sum14)
		i = i+1
		#db("Doc2", dict_sum21,dict_sum22,dict_sum23,dict_sum24)
	
read_data('/home/team3/Data/Unstructed_Data/agriculture/usAgriculture1.txt', 1, 998, "US Agriculture")

	
	
	
