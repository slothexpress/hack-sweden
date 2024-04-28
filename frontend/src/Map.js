import React, { useRef } from "react";
import {
  MapContainer,
  TileLayer,
  LayerGroup,
  CircleMarker,
  Polyline,
  Popup,
} from "react-leaflet";
import "leaflet/dist/leaflet.css";
// import { trails } from "./exampleData";
import { stations } from "./stationsTestData";

export default function Map(data) {
  console.log("🚀  🚀  🚀   ~ Map ~ data:", data);
  const mapRef = useRef(null);
  const latitude = 55.6918412;
  const longitude = 13.3603703;

  return (
    // Make sure you set the height and width of the map container otherwise the map won't show
    <MapContainer
      center={[latitude, longitude]}
      zoom={10}
      ref={mapRef}
      style={{ height: "50vh", width: "50vw" }}
    >
      <LayerGroup>
        {stations.map((station) => (
          <CircleMarker
            center={[station.coordinates[1], station.coordinates[0]]}
            radius={5}
            pathOptions={{ color: "red" }}
          >
            <Popup>{station?.name}</Popup>
          </CircleMarker>
        ))}
      </LayerGroup>
      <LayerGroup>
        {/* {data.map((trail) => (
          <Polyline positions={trail?.coordinates}>
            <Popup>{trail?.name}</Popup>
          </Polyline>
        ))} */}
      </LayerGroup>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
    </MapContainer>
  );
}
