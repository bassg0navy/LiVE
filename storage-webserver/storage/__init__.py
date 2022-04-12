from flask import Flask
import requests
import os
import oci



# MUST DEFINE APP HERE IN INIT.PY SO THAT SERVER CAN BE RAN FROM THE RUN.PY FILE
app = Flask(__name__) 

# ENVIRONMENT VARIABLES
PORT = os.environ.get('PORT')
PAR = 'https://objectstorage.us-ashburn-1.oraclecloud.com/p/hNZiv6tJIb_XThmFklLH4uqadlqGXcCE3YiG1sNY3aCaltQ-smCRkZm932HM8shk/n/id9ypxcsj7cu/b/streaming-videos/o/'

from storage import routes


