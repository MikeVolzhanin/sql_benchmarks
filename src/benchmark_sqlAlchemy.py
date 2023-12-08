from sqlalchemy import create_engine, text
from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
import time

engine = create_engine('sqlite:///../datasets/yellow.db')

def test(request):
    results_time = []
    
    for i in range(10):
        start = time.time() 
        with engine.connect() as conn:
            res = conn.execute(text(request))
        results_time.append(time.time() - start)
            
    return round(sum(results_time)/len(results_time), 2)

print("\nSQLAlchemy benchmark\n")
print("First SQL query: ")
print(test("SELECT VendorID, count(*) FROM yellow GROUP BY 1"))

print("Second SQL query: ")
print(test("SELECT passenger_count, avg(total_amount) FROM yellow GROUP BY 1"))

print("Third SQL query: ")
print(test("""
        SELECT passenger_count, strftime('%Y', tpep_pickup_datetime) AS pickup_year, COUNT(*)
        FROM yellow
        GROUP BY passenger_count, pickup_year
    """))

print("Fourth SQL query: ")
print(test("""SELECT passenger_count, 
                    strftime('%Y', tpep_pickup_datetime) AS pickup_year,
                    round(trip_distance),
                    count(*)
                    FROM yellow GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC"""
           ))


