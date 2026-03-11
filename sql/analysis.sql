SELECT COUNT(*)
FROM users;

SELECT city, COUNT(*)
FROM users
GROUP BY city:

SELECT platform, COUNT(*)
FROM users
GROUP BY platform;

SELECT city, AVG(purchase_amount)
FROM users
GROUP BY city;

SELECT platform, AVG(purchase_amount)
FROM users
GROUP BY platform
ORDER BY AVG(purchase_amount) DESC
LIMIT 1