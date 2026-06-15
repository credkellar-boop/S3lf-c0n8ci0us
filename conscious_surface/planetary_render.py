import pydeck as pdk

class PlanetaryRenderer:
    def __init__(self, resolution="8k"):
        self.resolution = resolution
        # NASA GIBS WMTS endpoint for high-res global imagery
        self.tile_url = "https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/BlueMarble_NextGeneration/default/2012-01-01/500m/{z}/{y}/{x}.jpg"

    def render_view(self, lat, lon, zoom):
        """Renders the planetary view utilizing the high-res textures."""
        return pdk.Deck(
            layers=[
                pdk.Layer(
                    "TileLayer", 
                    data=self.tile_url,
                    get_tile_data=lambda tile: self.tile_url.format(z=tile.z, y=tile.y, x=tile.x)
                )
            ],
            initial_view_state=pdk.ViewState(latitude=lat, longitude=lon, zoom=zoom)
        )
