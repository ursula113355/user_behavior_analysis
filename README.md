# User Behavior Analysis

## Dataset
Simulated dataset with 1000 users.

Columns
- age
- city
- platform
- purchase_amount
- visit_time

## Goal
Analyze user behavior and purchasing patterns.

## Analyze workflow
1. Generate dateset with python
2. Load data into SQLite database
3. Run SQL queries to analyze data
4. Import SQL result into pandas

## Analysis result

### Users per city
We analyzed the number of users in each city with SQL.

### Users per platform
We compared how many users use iOS, Android, Web.

### Average purchase by city
We calculated the average purchase amount of each city.

### Average purchase by platform
We analyzed which platform has the highest average purchase.

## Tech stack
- python
- pandas
- SQLite
- SQL

## Key findings
1. Users distribution across cities is relatively balanced and New York shows the highest purchase amount among all cities.
2. iOS users tend to have slightly lower average purchase amount.
3. Evening visits show the lowest average spending.