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
avg_purchase_city = pd.read_sql_query(query1, conn)
sns.set_theme()
sns.barplot(x="city", y="avg_purchase", data=avg_purchase_city)
plt.title("Average purchase by city")
plt.show()

query2 = """
SELECT platform, COUNT(*) as users
FROM users
GROUP BY platform
"""
user_platform = pd.read_sql_query(query2,conn)
sns.barplot(x="platform", y="users",data=user_platform)
plt.title("Users count by platform")
plt.show()

query3 = """
SELECT age
FROM users
GROUP BY age
"""
age_distribution = pd.read_sql_query(query3,conn)
sns.histplot(age_distribution["age"],bins=20)
plt.title("Age_distribution")
plt.show()

conn.close()