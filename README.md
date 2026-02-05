# Alternative Fueling Stations in the United States

<img width="7200" height="4800" alt="AndrewGilbertPosterUPDATED-1" src="https://github.com/user-attachments/assets/07163b5c-fdd4-49e7-a9f3-2c6e2a62b047" />

This poster was created using ArcGIS, Tableau, Excel, and adobe InDesign. 


Here is breakdown of what each software was used for:

ArcGIS:
- Creating the point maps
- Creating the non contiguous cartogram

Tableau:
- creating bar chart

Excel:
- cleaning data
- creating pie charts

InDesign:
- Compiling exports from ArcGIS, Tableau, & excel in to one place
- Adding text and layout


## Included in this repo is a folder called my work and folder called data.
### Data:
- alt_fuel_stations (Sep 26 2025).csv: contains all the points I used. Data was collected from https://afdc.energy.gov/data_download.
    - In excel I deleted any rows which contained data outside of the lower 48+DC, so theres 49 total "states." I did this for display purposes as the lower 48 is much easier to display.
- Parameters.png screenshot from the website containing exact parameters I used when downloading alt_fuel_stations (Sep 26 2025).csv
- Albersstates folder for Albersstates.shp: lower 48+DC for display purposes
    - I created this shape by using a publicly available shapefile of the US which contained populations for each state
    - I added a new column took the total number of stations in each state divided by population in each state(x100,000 for better display). This became the scaling factor for the cartogram
    - Reprojected the original states shapefile into albers for better display


### The folder with my work includes:
- bivariate_graph.twbx
      - A tableau workbook which shows exactly how I set up my variables. This can be opened in tableau reader which doesn't require a subscription but doesn't allow you to modify the workbook at all
          - notes:
              - ignore sheet 1 in the tableau workbook
              - sheet 2 was used for visualizing before exporting the graph.
              - sheet 3 is a copy of sheet 2 just with no background enabled, the sheet that I exported

- NonContiguous.py: python script for with comments for creating the cartogram
