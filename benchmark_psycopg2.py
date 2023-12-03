import psycopg2
import time

conn = psycopg2.connect(
    dbname="nyc_yellow_tiny",
    user="postgres",
    password="89194161213",
    host="localhost",
    port="5432"
)

cursor=conn.cursor()

def test(request):
    results_time = []
    for i in range(10):
        start = time.time()
        cursor.execute(request)
        results_time.append(time.time() - start)
    return round(sum(results_time)/len(results_time),2)

print("First SQL query: ")
print(test("SELECT passenger_count, avg(total_amount) FROM yellow_taxi GROUP BY 1"))

print("Second SQL query: ")
print(test("SELECT passenger_count, avg(total_amount) FROM yellow_taxi GROUP BY 1"))

print("Third SQL query: ")
print(test("""
        SELECT passenger_count, extract(year from tpep_pickup_datetime::timestamp) AS pickup_year, COUNT(*)
        FROM yellow_taxi
        GROUP BY passenger_count, pickup_year
    """))

print("Fourth SQL query: ")
print(test("""SELECT passenger_count, 
                    extract(year from tpep_pickup_datetime::timestamp) AS pickup_year,
                    round(trip_distance),
                    count(*)
                    FROM yellow_taxi GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC"""
           ))