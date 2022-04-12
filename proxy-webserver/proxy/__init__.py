from flask import Flask, redirect
#from sqlalchemy import create_engine, Column, Index, Integer, MetaData, Table
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.dialects import oracle
import requests
import cx_Oracle
import oci
import os
import sys
import datetime
import json

# MUST DEFINE APP HERE IN INIT.PY SO THAT SERVER CAN BE RAN FROM THE RUN.PY FILE
app = Flask(__name__)

# Initializing the Oracle DB Connection
cx_Oracle.init_oracle_client(lib_dir="/app/instantclient_21_5", config_dir="/app/instantclient_21_5/network/admin")
connection = cx_Oracle.connect(user="admin", password="$4THround4THround$", dsn="streamingdb1_high")

#username = "admin"
# set the password in an environment variable called "MYPW" for security
#password = os.environ.get("MYPW")
#dsn = "streamingdb1_high"
#engine = create_engine(
    #f'oracle://{username}:{password}@{dsn}/?encoding=UTF-8&nencoding=UTF-8', max_identifier_length=128)
#app.config['SQLALCHEMY_DATABASE_URI'] = engine
#db = SQLAlchemy(app)
#class VIDEO(db.Model):
    #VIDEO_ID = db.Column(db.Integer, primary_key=True)
    #VIDEO_NAME = db.Column(db.String(200), unique=True, nullable=False)
    #def __repr__(self):
        #return '<VIDEOS %r>' % self.VIDEO_NAME
    

# ENVIRONMENT VARIABLES
VIDEO_STORAGE_HOST = os.environ.get('VIDEO_STORAGE_HOST')
VIDEO_STORAGE_PORT = os.environ.get('VIDEO_STORAGE_PORT')

from proxy import routes, send