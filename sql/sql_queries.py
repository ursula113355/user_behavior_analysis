import sqlite3
import pandas as pd

conn = sqlite3.connect("data/users.db")

# 1 每个城市用户数量
query1 = """
SELECT city, COUNT(*) as users
FROM users
GROUP BY city
"""

city_users = pd.read_sql_query(query1, conn)
print("\nUsers per city: ")
print(city_users)

# 2 每个平台用户数量
query2 = """
SELECT platform, COUNT(*) as users
FROM users
GROUP BY platform
"""

platform_users = pd.read_sql_query(query2, conn)
print("\nUsers per platform: ")
print(platform_users)

# 3 每个城市平均消费
query3 = """
SELECT city, AVG(purchase_amount) as avg_purchase
FROM users
GROUP BY city
"""

avg_purchase_city = pd.read_sql_query(query3, conn)
print("\nAverage purchase per city: ")
print(avg_purchase_city)

# 4 哪个平台平均消费最高
query4 = """
SELECT platform, AVG(purchase_amount) as avg_purchase
FROM users
GROUP BY platform
ORDER BY AVG(purchase_amount) DESC
"""

platform_spending = pd.read_sql_query(query4, conn)
print("\nAverage purchase by platform: ")
print(platform_spending)

conn.close()
