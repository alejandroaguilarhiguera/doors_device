
import os
import time
from opening_door import opening_door 
from closing_door import closing_door 
from firebase_config import db

document_id = os.getenv("GOOGLE_DOCUMENT_ID")
collection = os.getenv("GOOGLE_COLLECTION")
doc_ref = db.collection(collection).document(document_id)

# TODO: Status GPIO
status_door = 'closed'

doc_ref.update({
    "status": status_door,
    "action": ""
})


def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        all_data = doc.to_dict()

        action = all_data['action']
        status = all_data['status']



        if (status == 'closed' and action == 'opening'):
            opening_door(doc_ref)

        if (status == 'opened' and action == 'closing'):
            closing_door(doc_ref)




doc_watch = doc_ref.on_snapshot(on_snapshot)

print("⏳ Escuchando cambios... Presiona Ctrl+C para salir.")
while True:
    time.sleep(1)
