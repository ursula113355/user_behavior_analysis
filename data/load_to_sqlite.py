import pandas as pd
import sqlite3

df = pd.read_csv("data/users.csv")
conn = sqlite3.connect("data/users.db")
df.to_sql("users", conn, if_exists="replace", index=False)
print("Data loaded into SQLite database.")
conn.close()
