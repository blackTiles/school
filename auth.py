import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyBw61BXRrmzddFfs-QOBoXfzkZZ-AA6Jz8",
    "authDomain": "rmsb-73b2e.firebaseapp.com",
    "projectId": "rmsb-73b2e",
    "storageBucket": "rmsb-73b2e.appspot.com",
    "messagingSenderId": "552149648469",
    "appId": "1:552149648469:web:4a43e2f85a5188a2f840dc",
    "measurementId": "G-NZ2WD5FBXN",
    "databaseURL": "rmsb-73b2e.asia-south1.firebasedatabase.app"
}

firebase = pyrebase.initialize_app(firebaseConfig)


auth = firebase.auth()
