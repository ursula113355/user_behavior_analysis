import sqlite3
import pandas as pd

conn = sqlite3.connect("data/users.db")

query = """
SELECT city, AVG(purchase_amount) as avg_purchase
FROM users
GROUP BY city
"""

df = pd.read_sql_query(query, conn)
print(df)

df.plot(x="city", y="avg_purchase", kind="bar", title="Average Purchase by city").get_figure().savefig("Average Purchase by city.png", bbox_inches="tight")


# 找最高消费城市
top_city = df.sort_values("avg_purchase", ascending=False).iloc[0]
print("\nCity with highest average purchase: ")
print(top_city)

conn.close()
