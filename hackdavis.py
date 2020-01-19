import os
import csv
import pandas as pd
credential_path = "C:\\Users\\ericn\\Desktop\\hackdavis2\\hack-davis-9ef6f-firebase-adminsdk-of8iz-75a124cfd6.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {'projectId': 'hack-davis-9ef6f',})

db = firestore.client()

input_file = pd.read_csv('listings2.csv')
result = input_file.to_dict('records')
for i in range(30):
  doc_ref = db.collection(u'apartments').add(result[i])
