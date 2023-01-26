import duckdb
import time

# Time initialization of DuckDB
duckdb_conn = duckdb.connect()
duckdb_conn.execute('SELECT 42')

start_time = time.time()
cursor = duckdb.connect()
initialization_time = time.time() - start_time
print("--- Initialization: %s seconds ---" % initialization_time)

# Time execution of a query
query_start_time = time.time()
print(cursor.execute('SELECT 42').fetchall())
query_end_time = time.time() - query_start_time
print("--- Query Exection: %s seconds ---" % query_end_time)