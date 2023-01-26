# duckdb_tests
DuckDB tests

# Installation

## Creating Python environment

python3 -m venv duckdb

➜  virtualenv cd duckdb
➜  duckdb ls
bin        include    lib        pyvenv.cfg
➜  duckdb source bin/activate

## Install DuckDB 0.6.1

duckdb $> pip install duckdb==0.6.1

(duckdb) ➜  duckdb pip install duckdb==0.6.1
Collecting duckdb==0.6.1
  Downloading duckdb-0.6.1-cp310-cp310-macosx_10_9_x86_64.whl (13.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.6/13.6 MB 7.7 MB/s eta 0:00:00
Collecting numpy>=1.14
  Downloading numpy-1.24.1-cp310-cp310-macosx_10_9_x86_64.whl (19.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 19.8/19.8 MB 6.0 MB/s eta 0:00:00
Installing collected packages: numpy, duckdb
Successfully installed duckdb-0.6.1 numpy-1.24.1
(duckdb) ➜  duckdb

## 