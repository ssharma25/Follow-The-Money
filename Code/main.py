from common_methods import read_file, tokenize_stem_file, remove_stopWords, get_frequency, read_csvDictionary, dict_sum, db

def read_data():

	#Read
	data1 = read_file('/home/team3/Data/Unstructed_Data/Inflow/Agro_Income.TXT')
	data2 = read_file('/home/team3/Data/Unstructed_Data/Inflow/Agro_Income1.TXT')
	data3 = read_file('/home/team3/Data/Unstructed_Data/Inflow/Agro_Influx.TXT')
	data4 = read_file('/home/team3/Data/Unstructed_Data/Inflow/Agro_Influx1.TXT')
	#data5 = read_file('/home/team3/Data/Unstructed_Data/Inflow/farmIncome.TXT')
	
	data6 = read_file('/home/team3/Data/Unstructed_Data/agriculture/usAgriculture1.txt')
	data7 = read_file('/home/team3/Data/Unstructed_Data/agriculture/usAgriculture2.txt')
	data8 = read_file('/home/team3/Data/Unstructed_Data/agriculture/usFarming1.TXT')
	data9 = read_file('/home/team3/Data/Unstructed_Data/agriculture/usFarming2.txt')
	
	#Documents
	doc1 = data1+data2+data3+data4
	#doc1 = data1
	
	doc2 = data6+data7+data8+data9
	#doc2 = data6
	
	#tokenize
	words1 = tokenize_stem_file(doc1)
	words2 = tokenize_stem_file(doc2)
	
	words1 = remove_stopWords(words1)
	words2 = remove_stopWords(words2)
	freq1 = get_frequency(words1)
	freq2 = get_frequency(words2)
	
	dict1 = read_csvDictionary('/home/team3/Data/Dictionaries/us_states1.csv')
	dict2 = read_csvDictionary('/home/team3/Data/Dictionaries/inflow.csv')
	dict3 = read_csvDictionary('/home/team3/Data/Dictionaries/outflow.csv')
	dict4 = read_csvDictionary('/home/team3/Data/Dictionaries/agriculture.csv')
	
	#for doc1
	dict_sum11 = dict_sum(dict1, doc1)
	dict_sum12 = dict_sum(dict2, doc1,'i')
	dict_sum13 = dict_sum(dict3, doc1,'i')
	dict_sum14 = dict_sum(dict4, doc1,'i')
	
	#for doc2
	dict_sum21 = dict_sum(dict1, doc2)
	dict_sum22 = dict_sum(dict2, doc2,'i')
	dict_sum23 = dict_sum(dict3, doc2,'i')
	dict_sum24 = dict_sum(dict4, doc2,'i')
	
	print("    ","dict1","dict2","dict3","dict4")
	print("Doc1",dict_sum11,dict_sum12,dict_sum13,dict_sum14)
	print("Doc2",dict_sum21,dict_sum22,dict_sum23,dict_sum24)
	
	db("Doc1", dict_sum11,dict_sum12,dict_sum13,dict_sum14)
	db("Doc2", dict_sum21,dict_sum22,dict_sum23,dict_sum24)
	
read_data()
	
	
	
