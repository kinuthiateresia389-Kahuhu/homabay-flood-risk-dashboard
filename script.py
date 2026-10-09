import folium
import pandas as pd

# 1. Read your data bundle directly using Pandas
df_combined_hb = pd.read_json("homabay_bundle.json")

# 2. Initialize your Map with the pristine Esri background tiles fix
m_hb = folium.Map(
    location=[-0.6, 34.5], 
    zoom_start=10, 
    tiles="https://arcgisonline.com{z}/{y}/{x}",
    attr="Esri ArcGIS"
)

# 3. Generate the Choropleth layer matching your columns directly
folium.Choropleth(
    geo_data="homabay_bundle.json",
    data=df_combined_hb,
    columns=["Ward Name", "Flood Hazard Area (%) (real)"],
    key_on="feature.properties.ward",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.5,
    line_color="black",
    legend_name="Flood Hazard Area (%)"
).add_to(m_hb)

# 4. Compile the final interactive file directly for GitHub Pages
m_hb.save("index.html")
print("Map successfully compiled!")
