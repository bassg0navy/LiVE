import cx_Oracle
from sqlalchemy import create_engine, Column, Index, Integer, MetaData, Table
from sqlalchemy.dialects import oracle
import sys
import os

# DB ENGINE CONNECTION
if sys.platform.startswith("darwin"):
    cx_Oracle.init_oracle_client(
        lib_dir=os.environ.get("HOME")+"/Downloads/instantclient_19_8",
        config_dir="")
elif sys.platform.startswith("win"):
    cx_Oracle.init_oracle_client(
        lib_dir=r"C:\Users\kabass\Oracle\instantclient-basiclite-windows.x64-21.3.0.0.0\instantclient_21_3")
# else assume system library search path includes Oracle Client libraries
# On Linux, use ldconfig or set LD_LIBRARY_PATH, as described in installation documentation.

username = "admin"
# set the password in an environment variable called "MYPW" for security
password = os.environ.get("MYPW")
dsn = "streamingdb1_high"

engine = create_engine(
    f'oracle://{username}:{password}@{dsn}/?encoding=UTF-8&nencoding=UTF-8', max_identifier_length=128)

with engine.connect() as conn:
    print(conn.scalar("select sysdate from dual"))
    

