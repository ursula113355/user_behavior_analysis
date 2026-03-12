import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

conn = sqlite3.connect("data/users.db")

query1 = """
SELECT city, AVG(purchase_amount) as avg_purchase
FROM users
GROUP BY city
"""
df = pd.read_sql_query(query1, conn)
sns.set_theme()
sns.barplot(x="city", y="avg_purchase", data=df)
plt.title("Average purchase by city")
plt.show()

query2 = """
SELECT platform, COUNT(*) as users
FROM users
GROUP BY platform
"""
df = pd.read_sql_query(query2,conn)
sns.barplot(x="platform", y="users",data=df)
plt.title("Users count by platform")
plt.show()

query3 = """
SELECT age
FROM users
GROUP BY age
"""
df = pd.read_sql_query(query3,conn)
sns.histplot(df["age"],bins=20)
plt.title("Age_distribution")
plt.show()

query4 = """
SELECT city, platform, AVG(purchase_amount) as avg_purchase
FROM users
GROUP BY city, platform
"""
df = pd.read_sql_query(query4, conn)
sns.barplot(x="city", y="avg_purchase", hue="platform", data=df)
plt.title("Average purchase by city and platform")
plt.show()

conn.close()