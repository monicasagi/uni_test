# Open file using the path from the directory presented as variable f
# File stored in variable which is instance of an object called "content"
with open(r'C:\Users\Monic\Desktop\sample.txt') as f:
	content = f.read()
print(content)

# storing the content in form of list
cnt_lst = []

# This module provides regular expression matching operations
import re

# Creating a dataframe by passing a list of objects
import pandas as pd

import sqlalchemy

# To define dataframe, and content in regular expression 
pattern = '\|(.*)\|'

# A regular expression to find all pattern & content
# re.findall(pattern, string, flags=0)
# Return all non-overlapping matches of pattern in string, as a list of strings
# re.IGNORECASE : This flag allows for case-insensitive matching of the Regular Expression with the given string 
# i.e. expressions like [A-Z] will match lowercase letters, too. Generally, It’s passed as an optional argument
ct = []
x = re.findall(pattern,content,re.IGNORECASE)
print(x)

# To put content in tabular format in pandas with dataframe using For loop
# Use pipe as delimiter to split the column
df_lst = pd.DataFrame([info.split("|") for info in x])
print(df_lst)

# Checking the index location of the content
df_lst.columns = df_lst.iloc[0]
print(df_lst)
df_lst = df_lst.drop(df_lst.index[0])
print(df_lst)

# Create connection to the sqlite database using create_engine
# The Engine is the starting point for any SQLAlchemy application. It’s “home base” for the actual database and its DBAPI, 
# delivered to the SQLAlchemy application through a connection pool and a Dialect, which describes how to talk to a specific kind of database/DBAPI combination.
# Reference : https://docs.sqlalchemy.org/en/13/core/engines.html
from sqlalchemy import create_engine

# Once our table(s) are defined and associated with our metadata object, 
# we need to create a database engine with which we can connect. This is accomplished using the create_engine function.
engine = create_engine('sqlite:///sqlalchemy_moni_example.db',echo=False)
print(engine)

# Writing pandas dataframe to SQLite table using "to_sql"
df_lst.to_sql('waste_data',con=engine)

# execute() method takes the SQL text or constructed SQL expression i.e. any of the variety of SQL expression constructs supported in SQLAlchemy 
# and returns query results (a ResultProxy - Wraps a DB-API cursor object to provide easier access to row columns.)
engine.execute('SELECT * from waste_data').fetchall()
