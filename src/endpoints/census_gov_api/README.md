## Census Geocoding API (notes)

Docs: https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html

This API can do:
- **Geocoding**: turn an address into coordinates + match metadata
- **GeoLookup** (optional): for a coordinate/address, return the matching geographies (state/county/tract/block/congressional district/etc.)

### Key parameters
- **returntype**:
  - **locations**: geocoding result only
  - **geographies**: geocoding result + geoLookup (geography layers)

- **searchtype**:
  - **onelineaddress**: one string address
  - **address**: split address parts
  - **addressPR**: Puerto Rico split address parts
  - **coordinates**: requires returntype=geographies; use x,y (lon,lat)

- **benchmark**: which locator dataset/version to search.
  - Can be **ID** or **name** from: https://geocoding.geo.census.gov/geocoder/benchmarks
  - Names look like DatasetType_SpatialBenchmark (example: Public_AR_Current)
    - DatasetType examples: Public_AR
    - SpatialBenchmark examples: Current, ACS####, Census####

- **vintage**: which geography vintage to use for geoLookup (**only needed for returntype=geographies**).
  - List vintages for a benchmark: https://geocoding.geo.census.gov/geocoder/vintages?benchmark=<benchmarkId>
  - Names look like GeographyVintage_SpatialBenchmark (example: Current_Current)
  - The SpatialBenchmark portion should match the chosen benchmark.

### Input parameters by searchtype
- **onelineaddress**:
  - address: full address string
- **address**:
  - street, city, state, zip
  - Minimum: street + zip OR street + city + state
- **addressPR**:
  - street, urb, city, municipio, state, zip
  - Minimum differs depending on whether you include an urbanization.
- **coordinates**:
  - x, y (longitude, latitude). Only returns geoLookup (geographies).

### Choosing “which geographies” with layers
When using returntype=geographies, you can specify **layers** to choose which geography layers are returned.

The layers values map to TIGERweb layer **IDs/names** (ArcGIS service). For the Current vintage:
- Service layer list: https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer

Example: congressional districts are currently:
- **119th Congressional Districts (54)** (use layers=54)
- 119th Congressional Districts Labels (55) (labels layer; usually not needed)

Direct layer pages:
- https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer/54
- https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer/55