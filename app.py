import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = st.secrets["mongodb_srv"]
client =  MongoClient(uri)


uri = "mongodb+srv://pigob32585_db_user:<db_password>@cluster0.iuc6qbl.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

st.title("Connected Successfully")

name = st.text_input("Emri","Emri")

if len(name) >= 3:
    st.write(name)