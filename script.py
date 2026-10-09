import folium
import json
import pandas as pd

# 1. Load your map data cleanly using Python's built-in json engine
with open("homabay_bundle.json", "r") as f:
    geo_data_hb = json.load(f)

# 2. Extract the statistical data from the JSON attributes into a DataFrame
features = geo_data_hb['features']
data_list = []
for f in features:
    props = f['properties']
    # Grabs the ward identifier and flood hazard value from your file properties
    data_list.append({
        "Ward Name": props.get("ward", props.get("Ward Name")),
        "Flood Hazard Area (%) (real)": props.get("Flood Hazard Area (%) (real)", 0)
    })
df_combined_hb = pd.DataFrame(data_list)

# 3. Initialize the Map with the pristine Esri background tiles fix
m_hb = folium.Map(
    location=[-0.6, 34.5], 
    zoom_start=10, 
    tiles="https://arcgisonline.com{z}/{y}/{x}",
    attr="Esri ArcGIS"
)

# 4. Generate the Choropleth layer
folium.Choropleth(
    geo_data=geo_data_hb,
    data=df_combined_hb,
    columns=["Ward Name", "Flood Hazard Area (%) (real)"],
    key_on="feature.properties.ward",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.5,
    line_color="black",
    legend_name="Flood Hazard Area (%)"
).add_to(m_hb)

# 5. Compile the final interactive file directly for GitHub Pages
m_hb.save("index.html")
print("Map successfully compiled without Geopandas!")
