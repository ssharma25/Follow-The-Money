from common_methodsArticles import read_file, tokenize_stem_file, remove_stopWords, get_frequency, read_csvDictionary, dict_sum, db, splitLexisNexis
from common_methodsArticles import articleDb, splitLexisNexis_AG, absoluteFilePaths, state_map
import re,numpy as np
import thread, time, sys

#To find exact integers
def string_to_int(value):
        m=re.search(r'[0-9]+.[0-9]*|[0-9]+',value)
        if m!=None:
                return float(m.group(0))
        else:
                return 1
#To etract exact integers from string including terms like million
#Also to add the stuff in DB
def clean_send_to_DB(state_full,project_name,money):
        money_dup=[]
        #print(state_full,project_name,money)
        for value in money:
                value=value.replace("dollar","").replace(" ","").replace(",","").replace("$","").replace("-","")
                if value.find('million')>-1:
                        value=string_to_int(value.replace("million",""))*10**6
                elif value.find('billion')>-1:
                        value=string_to_int(value.replace("billion",""))*10**12
                else:
                        value=string_to_int(value)
                money_dup.append(value)
        print(state_full,project_name,np.mean(money_dup))
        sys.stdout.flush()

def read_data(fp):
        articles = splitLexisNexis_AG(fp)
        dict1 = read_csvDictionary('/home/team3/Data/Dictionaries/us_states1.csv')
        dict2 = read_csvDictionary('/home/team3/Data/Dictionaries/us_states_shortname.csv')
        dict3 = read_csvDictionary('/home/team3/Data/Dictionaries/Project List.csv')
        dict4=[]
        for project in dict3:
                dict4.append(project.rstrip())

        for currentArticle in articles:
                state_full,project_name,m="","",""
                for state in dict1:
                        if currentArticle.count(state)>0:
                                state_full=state
                                project_name,m="",""
                                for project in dict4:
                                        if currentArticle.count(project)>0:
                                                #print(state,project)
                                                project_name=project
                                                #Regular Expresion for finding Money
                                                money=re.findall(r'\$ ?[0-9]+,[0-9]+,[0-9]+|\$ ?[0-9]+,[0-9]+|\$ ?[0-9]+ million|\$ ?[0-9]+ billion|million dollar|billion dollar|million-dollar|billion-dollar|\$ ?[0.9]+.[0-9]+ million|\$ ?[0.9]+.[0-9]+ billion|[0.9]+.[0-9]+ million dollar|[0.9]+.[0-9]+ million dollar', currentArticle.lower())
                                                if money!=[]:
                                                        clean_send_to_DB(state_map[state_full],project_name,money)

                state_full,project_name,m="","",""
                for state in dict2:
                        if currentArticle.count(state)>0:
                                state_full=state
                                project_name,m="",""
                                for project in dict4:
                                        if currentArticle.count(project)>0:
                                                #print(state,project)
                                                project_name=project
                                                #Regular Expresion for finding Money
                                                money=re.findall(r'\$ ?[0-9]+,[0-9]+,[0-9]+|\$ ?[0-9]+,[0-9]+|\$ ?[0-9]+ million|\$ ?[0-9]+ billion|million dollar|billion dollar|million-dollar|billion-dollar|\$ ?[0.9]+.[0-9]+ million|\$ ?[0.9]+.[0-9]+ billion|[0.9]+.[0-9]+ million dollar|[0.9]+.[0-9]+ million dollar', currentArticle.lower())
                                                if money!=[]:
                                                        clean_send_to_DB(state_full,project_name,money)
                """if state_full!="" and project_name!="" and m!="":
                        print(state_full,project_name,m)
                if state_full!="":
                        for project in dict4:
                                if currentArticle.count(project)>0:
                                        #print(state,project)
                                        project_name=project
                                        break
                m=re.findall(r'\$ ?[0-9]+,[0-9]+,[0-9]+|\$ ?[0-9]+,[0-9]+|\$ ?[0-9]{3}|\$ ?[0-9]+ million|\$ ?[0-9]+ billion|million dollar|billion dollar|million-dollar|billion-dollar', currentArticle)
                #re.match(r'\d+(?:,\d+)?',currentArticle)
                if m!=[]:
                        print(m)"""
                """if state_full!="" and project!="":
                        m=re.match('\-?\$?(?:(?:\d{1,3}(?:,+\d{3}){1,})|\d{4,})',currentArticle)
                        print(m)"""

gen=absoluteFilePaths('/home/team3/Data/Unstructed_Data/Projects/')
for i in gen:
        tup=(i)
        time.sleep(1)
        thread.start_new_thread(read_data,(i,))
        #print(i)
#read_data('/home/team3/Data/Unstructed_Data/agriculture/usAgriculture1.txt')
#read_data('/home/team3/Data/Unstructed_Data/agriculture/usAgriculture2.txt')
#read_data('/home/team3/Data/Unstructed_Data/agriculture/usFarming1.TXT')
#read_data('/home/team3/Data/Unstructed_Data/Projects/Loan1.TXT')
"""read_data('/home/team3/Data/Unstructed_Data/agriculture/usAgriculture1.txt', 1, 998)
read_data('/home/team3/Data/Unstructed_Data/agriculture/usAgriculture2.txt', 501, 998)
read_data('/home/team3/Data/Unstructed_Data/agriculture/usFarming1.TXT', 1, 1000)
read_data('/home/team3/Data/Unstructed_Data/agriculture/usFarming2.txt', 501, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Loan1.TXT', 1, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Loan2.TXT', 501, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Grants1.TXT', 1, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Grants2.TXT', 501, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Subsidy1.TXT', 1, 999)
read_data('/home/team3/Data/Unstructed_Data/Projects/Subsidy2.TXT', 501, 999)
read_data('/home/team3/Data/Unstructed_Data/Projects/Program1.TXT', 1, 999)
read_data('/home/team3/Data/Unstructed_Data/Projects/Program2.TXT', 501, 999)
read_data('/home/team3/Data/Unstructed_Data/agriculture/usFarming1.TXT', 1, 1000)
read_data('/home/team3/Data/Unstructed_Data/federalAid/federalAid1.txt', 1, 999)
read_data('/home/team3/Data/Unstructed_Data/federalAid/federalAid2.txt', 501, 999)
read_data('/home/team3/Data/Unstructed_Data/Inflow/Agro_Influx1.TXT', 500, 997)
read_data('/home/team3/Data/Unstructed_Data/Inflow/Agro_Influx.TXT', 1, 997)
read_data('/home/team3/Data/Unstructed_Data/Inflow/Agro_Income1.TXT', 1, 998)
read_data('/home/team3/Data/Unstructed_Data/Inflow/Agro_Income.TXT', 501, 998)
read_data('/home/team3/Data/Unstructed_Data/money/Fund_2.TXT', 501, 1000)
read_data('/home/team3/Data/Unstructed_Data/money/Fund_1.TXT', 1, 1000)
read_data('/home/team3/Data/Unstructed_Data/money/Cash_2.TXT', 501, 1000)
read_data('/home/team3/Data/Unstructed_Data/money/Cash_1.TXT', 1, 1000)
read_data('/home/team3/Data/Unstructed_Data/outflow/money_outflow_to_states_LN.TXT', 1, 999)
read_data('/home/team3/Data/Unstructed_Data/outflow/money_flow_to_states_for_agriculture_LN.TXT', 500, 999)


read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_15-53.TXT', 1, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_15-55.TXT', 501, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_15-58.TXT', 1, 998)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_15-59.TXT', 501, 996)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-06.TXT', 501, 998)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-12 2.TXT', 1, 90)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-12 3.TXT', 1, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-12.TXT', 1, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-13.TXT', 1, 997)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-14.TXT', 1, 12)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-15.TXT', 1, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-16 2.TXT', 501, 997)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-16 3.TXT', 501, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-16 4.TXT', 501, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-16.TXT', 501, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-19 2.TXT', 1, 996)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-19 3.TXT', 1, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-19 4.TXT', 1, 617)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-19 5.TXT', 1, 999)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-19 6.TXT', 1, 196)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-19.TXT', 1, 9)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-21.TXT', 501, 996)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-22 2.TXT', 501, 617)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-22 3.TXT', 501, 1000)
read_data('/home/team3/Data/Unstructed_Data/Projects/Company_Profiles_and_Directories_US_Law_Revi2017-03-31_16-22.TXT', 501, 1000)"""
	
	
	

