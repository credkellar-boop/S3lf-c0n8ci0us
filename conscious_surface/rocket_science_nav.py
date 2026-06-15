import math

class InterstellarNavigator:
    def __init__(self, gravitational_parameter_mu: float = 1.327e11): # Default: Sun (km^3/s^2)
        self.mu = gravitational_parameter_mu

    def calculate_vis_viva_velocity(self, current_radius: float, semi_major_axis: float) -> float:
        """Calculates instantaneous orbital velocity vector magnitude."""
        if current_radius <= 0 or semi_major_axis == 0:
            raise ValueError("Invalid orbital geometry parameters.")
        
        velocity_squared = self.mu * ((2.0 / current_radius) - (1.0 / semi_major_axis))
        return math.sqrt(max(0.0, velocity_squared))

    def compute_hohmann_transfer(self, r1: float, r2: float) -> tuple[float, float]:
        """Calculates delta-v requirements for a clean two-impulse orbital transfer."""
        dv1 = math.sqrt(self.mu / r1) * (math.sqrt((2 * r2) / (r1 + r2)) - 1.0)
        dv2 = math.sqrt(self.mu / r2) * (1.0 - math.sqrt((2 * r1) / (r1 + r2)))
        return dv1, dv2
