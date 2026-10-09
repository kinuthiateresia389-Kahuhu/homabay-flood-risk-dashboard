import folium
import json
import pandas as pd

# 1. Load your custom nested JSON file cleanly
with open("homabay_bundle.json", "r") as f:
    raw_json = json.load(f)

# 2. Extract the actual GeoJSON structure from your custom nested keys
geo_data_hb = raw_json["flood"]["wards"]

# 3. Extract the statistical rows into a clean data frame for Folium
features = geo_data_hb["features"]
data_list = []
for f in features:
    props = f["properties"]
    data_list.append({
        "Ward Name": props.get("Ward Name"),
        "Flood Hazard Area (%) (real)": props.get("Flood Hazard Area (%) (real)", 0.0)
    })
df_combined_hb = pd.DataFrame(data_list)

# 4. Initialize the Map with the pristine Esri background tiles fix
m_hb = folium.Map(
    location=[-0.6, 34.5], 
    zoom_start=10, 
    tiles="https://arcgisonline.com{z}/{y}/{x}",
    attr="Esri ArcGIS"
)

# 5. Generate the Choropleth layer using the precise data properties
folium.Choropleth(
    geo_data=geo_data_hb,
    data=df_combined_hb,
    columns=["Ward Name", "Flood Hazard Area (%) (real)"],
    key_on="feature.properties.Ward Name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.5,
    line_color="black",
    legend_name="Flood Hazard Area (%)"
).add_to(m_hb)

# 6. Add clean interactive hover tooltips for the dashboard
folium.GeoJson(
    geo_data_hb,
    name="Wards Data",
    style_function=lambda x: {'fillOpacity': 0, 'weight': 0},
    tooltip=folium.GeoJsonTooltip(
        fields=["Ward Name", "Total Population (real)", "Flood Hazard Area (%) (real)", "Estimated Population at Risk"],
        aliases=["Ward:", "Total Population:", "Flood Risk (%):", "Population at Risk:"],
        localize=True
    )
).add_to(m_hb)

# 7. Compile the final interactive file directly for GitHub Pages
m_hb.save("index.html")
print("Map successfully compiled with custom nested JSON data structure!")
