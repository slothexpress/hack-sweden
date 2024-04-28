from fastapi import APIRouter, HTTPException
import os
from dotenv import load_dotenv
import requests
import zipfile
import xml.etree.ElementTree as ET
import json
import uuid

router = APIRouter()

url = "https://opendata.samtrafiken.se/stopsregister-netex-sweden/sweden.zip?key="
xml_file = "resources/_stops.xml"
json_file= "resources/filtered_stops.json"

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

def extract_stop_places(root, namespace):
    latitude_boundary = 56.5512883
    stop_places = []
    num_saved = 0
    num_unsaved = 0
    for stop_place in root.findall('.//netex:StopPlace', namespace):
        name = stop_place.find('.//netex:Name', namespace).text
        longitude = float(stop_place.find('.//netex:Longitude', namespace).text)
        latitude = float(stop_place.find('.//netex:Latitude', namespace).text)
        transport_mode = stop_place.find('.//netex:TransportMode', namespace).text

        # Check if Latitude is below 56.5512883
        if latitude < latitude_boundary:
            unique_id = str(uuid.uuid4())
            stop_place_data = {
                "id": unique_id,
                "name": name,
                "coordinates": [latitude, 
                                longitude],
                "transport_mode": transport_mode
            }
            stop_places.append(stop_place_data)
            num_saved += 1
        else:
            num_unsaved += 1
    return stop_places, num_saved

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def xml_to_json():
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Define the namespace used in the XML file
    namespace = {'netex': 'http://www.netex.org.uk/netex'}

    # Extract and filter StopPlace data
    stop_places_data, num_saved = extract_stop_places(root, namespace)
    
    # Save the filtered data to a JSON file
    save_to_json(stop_places_data, json_file)

    # Print the number of elements saved
    print("Number of elements saved:", num_saved)
    return stop_places_data


@router.get("/stops")
async def get_stops():
    # data = test_fetch_api()
    
    # Read the JSON file
    with open(json_file, "r") as file:
        data = json.load(file)

    return data

@router.get("/json")
async def xml_json():
    stops = xml_to_json()
    return "XML TO JSON OK"

