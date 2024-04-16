from django.shortcuts import render
import pyrebase
 
config={
    "apiKey": "AIzaSyBuSqeVbAgTXoJUFYagzBb51qHDNIdeaMc",
    "authDomain": "taskify-685e0.firebaseapp.com",
    "projectId": "taskify-685e0",
    "storageBucket": "taskify-685e0.appspot.com",
    "messagingSenderId": "944801203349",
    "appId": "1:944801203349:web:a2318a5c65e24a3d01c79c",
    "measurementId": "G-BYR7R73E20",
    "databaseURL": "https://taskify-685e0-default-rtdb.asia-southeast1.firebasedatabase.app/"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()
 
def home(request):
    day = database.child('Data').child('Day').get().val()
    id = database.child('Data').child('Id').get().val()
    projectname = database.child('Data').child('Projectname').get().val()
    return render(request,"home.html",{"day":day,"id":id,"projectname":projectname })