#!/usr/bin/env python3

import argparse
import os
import subprocess
import uuid
import json
import ast
import datetime
import duckdb

batch = False

def main():
    parser = argparse.ArgumentParser(
        description='Retrieve metadata on deployed Dataflows'
    )

    parser.add_argument('--csv-directory', required=False, action="store", dest="csv_directory", help='Directory to search for CSV files')

    args = parser.parse_args()

   
    if args.csv_directory:
        csv_directory = args.csv_directory

    # Time initialization of DuckDB
    duckdb_conn = duckdb.connect()

    # get list of files in directory
    files = os.listdir(csv_directory)

    # loop through files
    for file in files:
        # create table
        query = "create table dataflows as select * FROM read_csv_auto('" + csv_directory + "/" + file + "')"
        # query to load CSV file into DuckDB
        #query = "insert into dataflows FROM read_csv_auto('" + csv_directory + "/" + file + "')"
        try:
            result = duckdb_conn.execute(query).fetchall()
        except Exception as e:
            print("Error: " + str(e))
            print("Query: " + query)

            if str(e) == 'Catalog Error: Table with name "dataflows" already exists!':
                print("Table already exists, insert data")
                query = "insert into dataflows FROM read_csv_auto('" + csv_directory + "/" + file + "')"
                result = duckdb_conn.execute(query).fetchall()

                print("Result: " + str(result))


            continue

        print("Result: " + str(result))

    # Dataflow Queries
    #print(duckdb_conn.execute("select * from dataflows").fetchall())

    # job_fields = "id,name,location,projectId,createTime,currentState,currentStateTime,environment.version.job_type,environment.version.major"
    print(duckdb_conn.execute("select * from dataflows").fetchall())

main()
