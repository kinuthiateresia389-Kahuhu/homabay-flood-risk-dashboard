# Homabay Flood Risk Dashboard

An interactive tool showing real, sourced flood exposure data for all 40 wards in Homa Bay County, Kenya.

## What it does
For each ward, this dashboard shows:
- Total population
- Building count (where available)
- Flood hazard area (% of ward at risk, 50-year return period)
- Estimated population and households at risk
- Estimated financial exposure (based on standard humanitarian cost estimates)

An interactive map visualizes flood risk across all wards, with wards shown in black where building data is still pending.

## Data sources
- **Population**: WorldPop 2020 constrained population estimates (data.worldpop.org)
- **Ward boundaries**: HDX / American Red Cross, "Administrative Wards in Kenya 1450"
- **Buildings**: OpenStreetMap (via OSMnx) — complete for most wards; some pending due to data source limitations
- **Flood hazard**: JRC (EU Joint Research Centre) Global River Flood Hazard Maps, 50-year return period

## Notes
Some building and flood values are marked as pending where data sources were unavailable at time of analysis — these are honestly labeled rather than estimated.

## Author
Teresia Kinuthia, Maseno University, School of Planning — Disaster Management with IT
