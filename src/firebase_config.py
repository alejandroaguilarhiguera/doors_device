import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv
from google.cloud import firestore

load_dotenv()

document_id = os.getenv("GOOGLE_DOCUMENT_ID")
collection = os.getenv("GOOGLE_COLLECTION")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./doors-6b438-firebase-adminsdk-fbsvc-d29712025e.json"

# Ruta al archivo JSON de tu cuenta de servicio
cred = credentials.Certificate("./doors-6b438-firebase-adminsdk-fbsvc-d29712025e.json")

firebase_admin.initialize_app(cred)

db = firestore.Client()
