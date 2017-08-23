#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="team3", user="team3", password="Toowie3a", host="152.1.26.117", port="5432")
cursor = conn.cursor()
cursor.execute("select * from ftm.project;")
print (cursor.fetchall())