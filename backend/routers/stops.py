from fastapi import APIRouter, HTTPException
import os
from dotenv import load_dotenv
import requests
import zipfile
import xml.etree.ElementTree as ET
import json
import uuid
from services.stops_service import StopsService

router = APIRouter()
stops_service = StopsService()

url = "https://opendata.samtrafiken.se/stopsregister-netex-sweden/sweden.zip?key="


def load_env_variables():
    dotenv_path = '../.env'
    load_dotenv(dotenv_path)

def test_fetch_api():
    load_env_variables()
    
    API_KEY = os.getenv("API_KEY_STOPS")
    
    # Make a GET request to the API
    response = requests.get(url + API_KEY)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()
        # Now you can work with the data as needed
        return data
    else:
        # If the request was not successful, print the error status code
        print("Error:", response.status_code)
        return "Can not fetch API from: " + url


@router.get("/stops")
async def get_stops():
    data = stops_service.get_stops()
    return data

@router.get("/json")
async def xml_json():
    stops_service.xml_to_json()
    return "XML TO JSON OK"

