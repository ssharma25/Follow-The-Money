from common_methodsArticles import read_file, tokenize_stem_file, remove_stopWords, get_frequency, read_csvDictionary, dict_sum, db, splitLexisNexis
from common_methodsArticles import articleDb, splitLexisNexis_AG, absoluteFilePaths, state_map
import re,numpy as np
from collections import Counter
#import thread, time, sys
import psycopg2

#Regular expression for corruption in states
def read_data(fp):
	#for each article
	articles = splitLexisNexis_AG(fp)
	states = read_csvDictionary('/home/team3/Data/Dictionaries/us_states1.csv')
	states_short = read_csvDictionary('/home/team3/Data/Dictionaries/us_states_shortname.csv')
	corruption = read_csvDictionary('/home/team3/Data/Dictionaries/corruption1.csv')
	agriculture = read_csvDictionary('/home/team3/Data/Dictionaries/agriculture.csv')
	result1 = {}
	result2 = {}
	cor_count = 0
	cor_count_short = 0
	        
	#regular expression for checking if corruption and getting count
	for currentArticle in articles:
		#For full forms
		re_states = re.findall(r"(?=("+'|'.join(states)+r"))",currentArticle)
		for each_state in re_states:
			#replacing short forms
			if each_state in states:
				i = states.index(each_state)
				a = states_short[i]
			ag_count = len(re.findall(r"(?=("+'|'.join(agriculture)+r"))",currentArticle))
			if ag_count > 0:
				global cor_count
				cor_count = len(re.findall(r"(?=("+'|'.join(corruption)+r"))",currentArticle))
				#print(cor_count)
			if cor_count > 0:
				result1[a] = cor_count
			else:
				continue
			
					
		#For short forms
		re_states_short = re.findall(r"(?=("+'|'.join(states_short)+r"))",currentArticle)
		for each_state_short in re_states_short:
			ag_count_short = len(re.findall(r"(?=("+'|'.join(agriculture)+r"))",currentArticle))
			if ag_count_short > 0:
				global cor_count_short
				cor_count_short = len(re.findall(r"(?=("+'|'.join(corruption)+r"))",currentArticle))
				#print(cor_count)
			if cor_count_short > 0:
				result2[each_state_short] = cor_count_short
					
	#To merge both dictionary values			
	A = Counter(result1)
	B = Counter(result2)
	
	result = A + B
	
	'''for k, v in result.items():
		print(k, v)'''
		
	return result
	
#read_data('/home/team3/Data/Unstructed_Data/corruption/black_money_02.TXT')

def read_files():
	result1 = read_data('/home/team3/Data/Unstructed_Data/corruption/crime_01.TXT')
	result2 = read_data('/home/team3/Data/Unstructed_Data/corruption/crime_02.TXT')
	result3 = read_data('/home/team3/Data/Unstructed_Data/corruption/fraud_01.TXT')
	result4 = read_data('/home/team3/Data/Unstructed_Data/corruption/fraud_02.TXT')
	result5 = read_data('/home/team3/Data/Unstructed_Data/corruption/delinquency_01.TXT')
	result6 = read_data('/home/team3/Data/Unstructed_Data/corruption/delinquency_02.TXT')
	result8 = read_data('/home/team3/Data/Unstructed_Data/corruption/exploit_01.TXT')
	result9 = read_data('/home/team3/Data/Unstructed_Data/corruption/exploit_02.TXT')
	result10 = read_data('/home/team3/Data/Unstructed_Data/corruption/fiddle_01.TXT')
	result11 = read_data('/home/team3/Data/Unstructed_Data/corruption/fiddle_02.TXT')
	result12 = read_data('/home/team3/Data/Unstructed_Data/corruption/graft_01.TXT')
	result13 = read_data('/home/team3/Data/Unstructed_Data/corruption/graft_02.TXT')
	result14 = read_data('/home/team3/Data/Unstructed_Data/corruption/laundering_01.TXT')
	result15 = read_data('/home/team3/Data/Unstructed_Data/corruption/laundering_02.TXT')
	result16 = read_data('/home/team3/Data/Unstructed_Data/corruption/misrepresent_01.TXT')
	result17 = read_data('/home/team3/Data/Unstructed_Data/corruption/misrepresent_02.TXT')
	result18 = read_data('/home/team3/Data/Unstructed_Data/corruption/racket_01.TXT')
	result19 = read_data('/home/team3/Data/Unstructed_Data/corruption/racket_02.TXT')
	result20 = read_data('/home/team3/Data/Unstructed_Data/corruption/offence_01.TXT')
	result21 = read_data('/home/team3/Data/Unstructed_Data/corruption/offence_02.TXT')
	result22 = read_data('/home/team3/Data/Unstructed_Data/corruption/tax_evasion_01.TXT')
	result23 = read_data('/home/team3/Data/Unstructed_Data/corruption/tax_evasion_02.TXT')
	result24 = read_data('/home/team3/Data/Unstructed_Data/corruption/bribe_01.TXT')
	result25 = read_data('/home/team3/Data/Unstructed_Data/corruption/bribe_02.TXT')
	result26 = read_data('/home/team3/Data/Unstructed_Data/corruption/black_money_01.TXT')
	result27 = read_data('/home/team3/Data/Unstructed_Data/corruption/black_money_02.TXT')
	result28 = read_data('/home/team3/Data/Unstructed_Data/corruption/misconduct_01.TXT')
	result29 = read_data('/home/team3/Data/Unstructed_Data/corruption/misconduct_02.TXT')
	result30 = read_data('/home/team3/Data/Unstructed_Data/corruption/wrongdoing_01.TXT')
	result31 = read_data('/home/team3/Data/Unstructed_Data/corruption/wrongdoing_02.TXT')
	
	A = Counter(result1)+Counter(result2)+Counter(result3)+Counter(result4)+Counter(result5)+Counter(result6)+Counter(result8)+Counter(result9)+Counter(result10)+Counter(result11)+Counter(result12)+Counter(result13)+Counter(result14)+Counter(result15)+Counter(result16)+Counter(result17)+Counter(result18)
	B = Counter(result19)+Counter(result20)+Counter(result21)+Counter(result22)+Counter(result23)+Counter(result24)+Counter(result25)+Counter(result26)+Counter(result27)+Counter(result28)+Counter(result29)+Counter(result30)+Counter(result31)	
	
	results = Counter(A) + Counter(B)
	return results
	
#Inserting data into database
def insertDBCorruption():
	try:
		conn = psycopg2.connect("dbname='team3' user='team3' host='localhost' password='Toowie3a'")
		cur = conn.cursor()
		result = read_files()
		for k, v in result.items():
			print(k, v)
			query = "Insert into ftm.corruption values(%s,%s)"
			data = (k,v)
			cur.execute(query, data)
		conn.commit()
		conn.close()
		
	except:
		print("error")
		
insertDBCorruption()
	