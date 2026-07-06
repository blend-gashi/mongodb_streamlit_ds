import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = st.secrets["mongodb_srv"]
client =  MongoClient(uri)

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

st.title("Connected Successfully")

# Client eshte streamlitMongodb, emri i tabelezes
server = MongoClient(uri)
server.admin.command('ping')
db = server['name_tracker']
collection = db["usernames"]

db = client["name_tracker"]
collection = db["usernames"]



print("Inserted")

name = st.text_input("Emri","Emri")

if len(name) >= 3:
    collection.insert_one({
    "name": name
})
else:
    st.write("Name is too short")