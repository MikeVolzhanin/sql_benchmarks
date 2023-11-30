import sqlite3
import time

conn = sqlite3.connect('yellow_taxi.db')

cursor = conn.cursor()

#first
start = time.time()
cursor.execute("SELECT passenger_count, avg(total_amount) FROM yellow_taxi GROUP BY 1")
end = time.time() - start
print("First SQL query: ")
print(end)

#second
start = time.time()
cursor.execute("SELECT passenger_count, avg(total_amount) FROM yellow_taxi GROUP BY 1")
end = time.time() - start
print("Second SQL query: ")
print(end)

#third
start = time.time()
cursor.execute("""
    SELECT passenger_count, strftime('%Y', tpep_pickup_datetime) AS pickup_year, COUNT(*)
    FROM yellow_taxi
    GROUP BY passenger_count, pickup_year
""")
end = time.time() - start
print("Third SQL query: ")
print(end)

#fourth
start = time.time()
cursor.execute("""SELECT passenger_count, 
                strftime('%Y', tpep_pickup_datetime) AS pickup_year,
                round(trip_distance),
                count(*)
                FROM yellow_taxi GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC""")
end = time.time() - start
print("Fourth SQL query: ")
print(end)

results = cursor.fetchall()
conn.close()

