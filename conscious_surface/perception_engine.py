from .planetary_render import PlanetaryRenderer
from .autonomous_nav import WaymoNavigator

class PerceptionEngine:
    def __init__(self):
        self.geo = PlanetaryRenderer()
        self.nav = WaymoNavigator()

    def sync_inputs(self, spatial_data, lidar_data):
        # Fuses 8K planet visuals with LiDAR obstacle data
        map_view = self.geo.render_view(spatial_data['lat'], spatial_data['lon'], 10)
        safety_vector = self.nav.process_point_cloud(lidar_data)
        return {"map": map_view, "safety": safety_vector}
