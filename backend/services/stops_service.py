import json
import xml.etree.ElementTree as ET
import uuid

class StopsService:
    xml_file = "resources/_stops.xml"
    json_file= "resources/filtered_stops.json"

    def extract_stop_places(self, root, namespace):
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

    def save_to_json(self, data, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def xml_to_json(self):
        # Parse the XML file
        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        # Define the namespace used in the XML file
        namespace = {'netex': 'http://www.netex.org.uk/netex'}

        # Extract and filter StopPlace data
        stop_places_data, num_saved = self.extract_stop_places(root, namespace)
        
        # Save the filtered data to a JSON file
        self.save_to_json(stop_places_data, self.json_file)

        # Print the number of elements saved
        print("Number of elements saved:", num_saved)
        return stop_places_data
    
    def get_stops(self):
        # Read the JSON file
        with open(self.json_file, "r") as file:
            data = json.load(file)
        return data