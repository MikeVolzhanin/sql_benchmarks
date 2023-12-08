import os

print("""
      What library/libraries do you want to test?\n
      1)SQLite\n
      2)DuckDB\n
      3)Psycopg2\n
      4)Pandas\n
      5)SQLAlchemy
      """)

libraries = ["benchmark_sqlite.py","benchmark_duckDB.py","benchmark_psycopg2.py","benchmark_pandas.py","benchmark_sqlAlchemy.py",]
result = input()
start_str = ""

for i in range(len(result)):
    if i == len(result) - 1:
        start_str += ("python " + libraries[int(result[i])-1])
    else:
        start_str += ("python "+ libraries[int(result[i])-1] + " && ")

# print(start_str)

os.system(start_str)


