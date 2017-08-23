from common_methodsArticles import read_file, tokenize_stem_file, remove_stopWords, get_frequency, read_csvDictionary, dict_sum, db, splitLexisNexis
from common_methodsArticles import articleDb, splitLexisNexis_AG, absoluteFilePaths, state_map
import re,numpy as np
import thread, time, sys, psycopg2

#Need to use python2 as python3 doesn't have thread library installed

#print(state_map)

#To find exact integers
def string_to_int(value):
        m=re.search(r'[0-9]+.[0-9]*|[0-9]+',value)
        if m!=None:
                return float(m.group(0))
        else:
                return 1

#Inserting data into database
def insertDBInflow(state,money):
        try:
                conn = psycopg2.connect("dbname='team3' user='team3' host='localhost' password='Toowie3a'")
                cur = conn.cursor()
                query = "Insert into ftm.inflow values (%s,%s)"
                data = (state,money)
                cur.execute(query, data)
                conn.commit()
                conn.close()
        except:
                print("error")

#To extract exact integers from string including terms like million
#Also to add the stuff in DB
def clean_send_to_DB(state,money):
        money_dup=[]
        #print(state,money)
        for value in money:
		#print (state,value)
                value=value.replace("dollar","").replace(" ","").replace(",","").replace("$","").replace("-","")
                if value.find('million')>-1:
                        value=string_to_int(value.replace("million",""))*10**6
                elif value.find('billion')>-1:
                        value=string_to_int(value.replace("billion",""))*10**12
                else:
                        value=string_to_int(value)
                money_dup.append(value)
        """insertDBInflow(state,np.mean(money_dup))"""
        print(state,np.mean(money_dup))
        #sys.stdout.flush()

def read_data(fp):
	articles = splitLexisNexis_AG(fp)
        dict1 = read_csvDictionary('/home/team3/Data/Dictionaries/us_states1.csv')
        dict2 = read_csvDictionary('/home/team3/Data/Dictionaries/us_states_shortname.csv')
        dict3 = read_csvDictionary('/home/team3/Data/Dictionaries/inflow.csv')
        dict4 = read_csvDictionary('/home/team3/Data/Dictionaries/agriculture.csv')

	for currentArticle in articles:
		state_full = ""
                
		for state in dict1:
			
		        if currentArticle.count(state)>0:
				
				state_full = state
                    
		                if state_full!= " " and state_full!="" and dict_sum(dict3,currentArticle)>0 and dict_sum(dict4,currentArticle)>0:
                                       money=re.findall(r'\$ [0-9]+,[0-9]+,[0-9]+|\$ [0-9]+,[0-9]+|\$ [0-9]+ million|\$ [0-9]+ billion|\$ ?[0.9]+.[0-9]+ million|\$ ?[0.9]+.[0-9]+ billion|[0.9]+.[0-9]+ million dollar|[0.9]+.[0-9]+ million dollar', currentArticle.lower())
                                if money!=[]:
                                       clean_send_to_DB(state_map[state_full],money)

                
                state_full = ""
                for state in dict2:
                        
                        if currentArticle.count(state)>0:
				
				state_full = state
                    
		                if state_full!= " " and state_full!="" and dict_sum(dict3,currentArticle)>0 and dict_sum(dict4,currentArticle)>0:
                                       money=re.findall(r'\$ [0-9]+,[0-9]+,[0-9]+|\$ [0-9]+,[0-9]+|\$ [0-9]+ million|\$ [0-9]+ billion|\$ ?[0.9]+.[0-9]+ million|\$ ?[0.9]+.[0-9]+ billion|[0.9]+.[0-9]+ million dollar|[0.9]+.[0-9]+ million dollar', currentArticle.lower())
                                if money!=[]:
                                       clean_send_to_DB(state_full,money)


gen=absoluteFilePaths('/home/team3/Data/Unstructed_Data/Projects/')
for i in gen:
        time.sleep(1)
        #read_data(i)
        thread.start_new_thread(read_data,(i,))

"""UPDATE query to find average
update ftm.inflow SET state = subquery.state,funds = subquery.funds FROM (select state, avg(funds) AS funds from ftm.inflow GROUP BY 1) AS subquery where ftm.inflow.state = subquery.state;

Query to find inflow-outflow
select ftm.inflowFunds.state, ftm.inflowFunds.funds - ftm.outflowFunds.funds from ftm.inflowFunds inner join ftm.outflowFunds on ftm.inflowFunds.state = ftm.outflowFunds.state;

Query To create new table of distinct elements
CREATE TABLE ftm.tmpIn AS SELECT DISTINCT * FROM ftm.inflow;"""
        