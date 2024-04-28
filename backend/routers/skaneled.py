from fastapi import APIRouter, Response
from urllib import request
import geopandas as gpd

router = APIRouter()

@router.get("/skaneled")
async def get_skaneled():
    webFile = request.urlopen("https://raw.githubusercontent.com/perliedman/skaneleden/main/src/data/skaneleden.json").read()
    jsonContent = webFile.decode('utf-8')

    gdf = gpd.read_file(jsonContent, driver='GeoJSON')
    smaller = gdf[gdf["bus"] != "Yes"]
    smaller = smaller.get(['name', 'from', 'to', 'geometry', 'website'])

    return Response(smaller.to_json())
