import { useState } from "react";

const API_URL = "http://localhost";
const API_PORT = "8000";

async function useGetData() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const reverseCoordinates = (features) => {
    console.log("🚀  🚀  🚀   ~ useGetData ~ features:", features);
    //   return

    // features.map((feature) => {
    //   const { geometry, properties } = feature;
    //   const coordinates = geometry?.coordinates.map((coordinate) => [
    //     coordinate[1],
    //     coordinate[0],
    //   ]);
    //   return { name: properties?.name, coordinates };
    // });
  };

  try {
    const trailsData = await fetch(`${API_URL}:${API_PORT}/skaneled`);
    // const stopsData = await fetch(`${API_URL}:${API_PORT}/`);
    // console.log("🚀  🚀  🚀   ~ fetchData ~ stopsData:", stopsData);
    const jsonData = await trailsData.json();
    const trails = reverseCoordinates(jsonData);
    console.log("🚀  🚀  🚀   ~ fetchData ~ trails:", trails);
    setData(trails);
  } catch (error) {
    setError(error);
    console.error("Error fetching data:", error);
  } finally {
    setLoading(false);
  }
  return { data, loading, error };
}

export default useGetData;
