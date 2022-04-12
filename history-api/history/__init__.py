from flask import Flask, redirect
from celery import Celery
import requests, os, sys, cx_Oracle, oci, json, datetime


# MUST DEFINE APP HERE IN INIT.PY SO THAT SERVER CAN BE RAN FROM THE RUN.PY FILE
app = Flask(__name__)

# Initializing the Oracle DB Connection
cx_Oracle.init_oracle_client(lib_dir="/app/instantclient_21_5", config_dir="/app/instantclient_21_5/network/admin")
connection = cx_Oracle.connect(user="admin", password="$4THround4THround$", dsn="streamingdb1_high", threaded='true')

# ENVIRONMENT VARIABLES
VIDEO_STORAGE_HOST = os.environ.get('VIDEO_STORAGE_HOST')
VIDEO_STORAGE_PORT = os.environ.get('VIDEO_STORAGE_PORT')

from history import routes, receive
