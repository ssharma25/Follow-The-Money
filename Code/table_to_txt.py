import sys

#set up psycopg2 environment
import psycopg2

#driving_distance module
#note the lack of trailing semi-colon in the query string, as per the Postgres documentation
query = """
            select
            state as state,
            funds as funds
        from ftm.outflowFunds
"""

#make connection between python and postgresql
conn = psycopg2.connect("dbname='team3' user='team3' host='localhost' password='Toowie3a'")
cur = conn.cursor()

outputquery = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)

with open('outflowfile', 'w') as f:
    cur.copy_expert(outputquery, f)

conn.close()