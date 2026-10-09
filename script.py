import folium
import pandas as pd
import geopandas as gpd

# ---- ADD THESE MISSING LINES RIGHT HERE ----
# This loads your map boundaries from your repository files
homabay_wards = gpd.read_file("homabay_bundle.json") 

# This loads your population risk data sheet
df_combined_hb = pd.read_csv("your_data_file.csv") # Make sure this matches your actual file name!
# --------------------------------------------

# Replace your folium.Map initialization line with this:
m_hb = folium.Map(
    location=[-0.6, 34.5], 
    zoom_start=10, 
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
    attr="Esri ArcGIS"
)
merged_hb = homabay_wards.merge(df_combined_hb, left_on="ward", right_on="Ward Name")
folium.Choropleth(
    geo_data=merged_hb, data=merged_hb,
    columns=["Ward Name", "Flood Hazard Area (%) (real)"],
    key_on="feature.properties.ward",
    fill_color="YlOrRd", fill_opacity=0.8, line_opacity=0.5, line_color="black",
    legend_name="Flood Hazard Area (%) — darker red = higher flood risk",
    bins=[0, 1, 5, 10, 20, 35]
).add_to(m_hb)
folium.GeoJson(
    merged_hb, style_function=lambda x: {"fillColor": "transparent", "color": "transparent"},
    tooltip=folium.GeoJsonTooltip(
        fields=["Ward Name", "Total Population (real)", "Flood Hazard Area (%) (real)", "Estimated Population at Risk"],
        aliases=["Ward:", "Population:", "Flood Risk %:", "Population at Risk:"], localize=True
    )
).add_to(m_hb)
m_hb.save("homabay_flood_risk_map.html")
print("Homabay map saved!")
m_hb.save("index.html")
print("Map successfully compiled!")
