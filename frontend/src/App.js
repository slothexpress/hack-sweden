import React, { useEffect, useState } from "react";
import "./App.css";

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
        <div>
          <h1>Data from Backend API:</h1>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      </header>
    </div>
  );
}

export default App;
