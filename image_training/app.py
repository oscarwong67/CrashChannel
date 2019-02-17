from flask import Flask
from flask import request
from flask_cors import CORS
from label_image import *
from apscheduler.schedulers.background import BackgroundScheduler
import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./calgaryhacks-2019-mibros-521ab-firebase-adminsdk-iafo3-7b4618381a.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

import urllib

COLLECTION = "demoCameras"
THRESHOLD = 0.30
UPDATE_INTERVAL = 3

app = Flask(__name__)
CORS(app)

def db_request():
    collection = db.collection(COLLECTION).get()
    for doc in collection :
        imageURL = doc.to_dict().get("imageURL")
        res = runModel(imageURL)
        doc_ref = db.collection(COLLECTION).document(doc.id)
        if (float(res["crashes"]) > THRESHOLD) :
            doc_ref.update({
                "crashData": {
                    "isCrash": True,
                    "percentCrash": float(res["crashes"]),
                    "percentNormal": float(res["normal traffic"])
                }
            })
        else :
            doc_ref.update({
                "crashData": {
                    "isCrash": False,
                    "percentCrash": float(res["crashes"]),
                    "percentNormal": float(res["normal traffic"])
                }
            })
        print(str(res))

@app.route('/test')
def index():
    url = request.args.get('img')
    url = urllib.parse.unquote(url)

    return json.dumps(runModel(url))

if __name__ == "__main__":
  scheduler = BackgroundScheduler()
  scheduler.add_job(func=db_request, trigger="interval", minutes=UPDATE_INTERVAL)
  scheduler.start()
  app.run()

