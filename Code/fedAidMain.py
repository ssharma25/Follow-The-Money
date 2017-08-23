from fedAidMethods import read_file, tokenize_stem_file, remove_stopWords, get_frequency, read_csvDictionary, dict_sum, db, splitLexisNexis, fedAidDb

def analyzeFedAid(fp, start, end, docname):
	articles = splitLexisNexis(fp, start, end)
	
	stateAvg = 5.02
	govAvg = 5.94
	aidAvg = 11.82
	agAvg = 3.34
	
	i = start
	for currentArticle in articles:
		#tokenize
		words1 = tokenize_stem_file(currentArticle)
		#words2 = tokenize_stem_file(doc2)
		
		words1 = remove_stopWords(words1)
		#words2 = remove_stopWords(words2)
		freq1 = get_frequency(words1)
		#freq2 = get_frequency(words2)
		
		dict1 = read_csvDictionary('/home/team3/Data/Dictionaries/us_states1.csv')
		dict2 = read_csvDictionary('/home/team3/Data/Dictionaries/federalGov.csv')
		dict3 = read_csvDictionary('/home/team3/Data/Dictionaries/outflow.csv')
		dict4 = read_csvDictionary('/home/team3/Data/Dictionaries/agriculture.csv')
		
		#for doc1
		stateSum = dict_sum(dict1, currentArticle)
		govSum = dict_sum(dict2, currentArticle,'i')
		aidSum = dict_sum(dict3, currentArticle,'i')
		agSum = dict_sum(dict4, currentArticle,'i')
		
		score = stateSum / stateAvg * 5 + govSum / govAvg * 2 + aidSum / aidAvg * 5 + agSum / agAvg * 5
		
		#for doc2
		#dict_sum21 = dict_sum(dict1, doc2)
		#dict_sum22 = dict_sum(dict2, doc2,'i')
		#dict_sum23 = dict_sum(dict3, doc2,'i')
		#dict_sum24 = dict_sum(dict4, doc2,'i')
		
		#print("    ","dict1","dict2","dict3","dict4")
		#print("Doc1",dict_sum11,dict_sum12,dict_sum13,dict_sum14)
		#print("Doc2",dict_sum21,dict_sum22,dict_sum23,dict_sum24)
		if score > 35:
			fedAidDb(docname + str(i), stateSum, govSum, aidSum, agSum)
		i = i+1
		#db("Doc2", dict_sum21,dict_sum22,dict_sum23,dict_sum24)
	
#read_data('/home/team3/Data/Unstructed_Data/agriculture/usAgriculture1.txt', 1, 998, "US Agriculture")
#read_data('/home/team3/Data/Unstructed_Data/agriculture/usAgriculture2.txt', 501, 998, "US Agriculture")
#read_data('/home/team3/Data/Unstructed_Data/agriculture/usFarming1.TXT', 1, 1000, "US Farming")
#read_data('/home/team3/Data/Unstructed_Data/agriculture/usFarming2.txt', 501, 1000, "US Farming")
#read_data('/home/team3/Data/Unstructed_Data/Inflow/Agro_Influx.TXT', 1, 997, "Agriculture Inflow")
#read_data('/home/team3/Data/Unstructed_Data/Inflow/Agro_Influx1.TXT', 500, 997, "Agriculture Inflow")
#read_data('/home/team3/Data/Unstructed_Data/Inflow/Agro_Income.TXT', 500, 998, "Agriculture Income")
#read_data('/home/team3/Data/Unstructed_Data/Inflow/Agro_Income1.TXT', 1, 998, "Agriculture Income")

analyzeFedAid('/home/team3/Data/Unstructed_Data/federalAid/federalAid1.txt', 1, 999, "US Federal Aid Article ")
analyzeFedAid('/home/team3/Data/Unstructed_Data/federalAid/federalAid2.txt', 501, 999, "US Federal Aid Article ")

	
	
	
