#install.packages("RPostgreSQL")
require("RPostgreSQL")
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = "team3",host = "localhost", port = 5432,
                 user = "team3", password = "Toowie3a")
project <- dbGetQuery(con, "SELECT * from ftm.project")
colnames(project)[3]<-"estfunds"
#print(project)
project_unique<-dbGetQuery(con, "SELECT distinct state,project_name from ftm.project")
#print(project_unique)

drought<- dbGetQuery(con, "select state_short as state,
CAST(nullif(primarycounties, '') AS integer)
+CAST(nullif(contiguouscounties, '') AS integer) as effectedcounties 
from ftm.droughtstatewisedata,
ftm.states where state=state_full")

table1<-merge(project,drought,by="state")

inflowfunds <- dbGetQuery(con, "SELECT * from ftm.inflowfunds")
table1<-merge(table1,inflowfunds,by="state")

outflowfunds <- dbGetQuery(con, "SELECT * from ftm.outflowfunds")
table1<-merge(table1,outflowfunds,by="state")


taxbystate<-dbGetQuery(con, "SELECT state_short as state, amount
                      from ftm.taxesbystate, ftm.states
                       where state_full=geographic_area_name")
table1<-merge(table1,taxbystate,by="state")

# farmincome<-dbGetQuery(con,"select state,description,avg(amount)
#                         from ftm.farmincome2017
#                        group by state,description")
# table1<-merge(table1,farmincome,by="state")
print(head(table1))

lm.model<-lm(estfunds~.,data = table1)
est<-predict(lm.model,newdata=unique(table1[,-3]))
big_table<-data.frame(unique(table1[,-3]),est)
print(head(big_table))
#select column_name, data_type from information_schema.columns where table_name = 'config';

# state_list<-read.csv('/home/team3/Data/Dictionaries/us_states.csv',sep=",",header=FALSE)
# print(state_list)
# dbWriteTable(con, c("ftm","states"), 
#           value = state_list,append=TRUE, row.names = FALSE)

