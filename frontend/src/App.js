import React, { useEffect, useState } from "react";
import "./App.css";
import Map from "./Map";
import FilterForm from "./FilterForm";

const API_URL = "http://localhost";
const API_PORT = "8000";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch(`${API_URL}:${API_PORT}`);
      const jsonData = await response.json();
      setData(jsonData);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <div
          style={{
            display: "flex",
            gap: "50px",
          }}
        >
          <FilterForm />
          <Map />
        </div>
      </header>
    </div>
  );
}

export default App;
