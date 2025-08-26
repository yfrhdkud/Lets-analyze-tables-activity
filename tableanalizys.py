import sqlite3 as sql
import pandas as pd

database = "database.sqlite"
conn =  sql.connect(database)
print("Opened data successfully")

tables = pd.read_sql("""
  SELECT * FROM sqlite_master WHERE type = 'tables';        
                    """,conn)

matches = pd.read_sql("""
SELECT * FROM Match;
                      """,conn)

matches.info()
