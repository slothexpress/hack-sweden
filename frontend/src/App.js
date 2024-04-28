import React, { useEffect } from "react";
import "./App.css";
import Map from "./Map";
import FilterForm from "./FilterForm";
import useGetData from "./useGetData";

function App() {
  const { data, loading, error } = useGetData();

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
          {!loading && <Map data={data} />}
        </div>
      </header>
    </div>
  );
}

export default App;
