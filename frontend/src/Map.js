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
import { trails } from "./exampleData";

const Map = () => {
  const mapRef = useRef(null);
  const latitude = 55.6918412;
  const longitude = 13.3603703;
  const busStops = [
    [55.695, 13.36038],
    [55.6966, 13.36038],
    [55.697, 13.36038],
    [55.698, 13.36038],
  ];

  return (
    // Make sure you set the height and width of the map container otherwise the map won't show
    <MapContainer
      center={[latitude, longitude]}
      zoom={10}
      ref={mapRef}
      style={{ height: "50vh", width: "50vw" }}
    >
      <LayerGroup>
        {busStops.map((coordinates) => (
          <CircleMarker
            center={coordinates}
            radius={5}
            pathOptions={{ color: "red" }}
          ></CircleMarker>
        ))}
      </LayerGroup>
      <LayerGroup>
        {trails.map((trail) => (
          <Polyline positions={trail?.coordinates}>
            <Popup>{trail?.name}</Popup>
          </Polyline>
        ))}
      </LayerGroup>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {/* Additional map layers or components can be added here */}
    </MapContainer>
  );
};

export default Map;
