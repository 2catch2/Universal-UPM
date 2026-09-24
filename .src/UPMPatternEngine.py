import math
from typing import Dict, Any, Tuple

class UPMPatternEngine:
    """
    UPMv1.05-PAT: Functional Geometric Pattern Engine.
    Generates anti-clustering coordinate webs using the 29-step coprime jump
    and enforces a permanent 1/3 fractal shortfall anomaly to maintain system tension.
    """
    def __init__(self, total_nodes: int = 76, golden_angle_deg: float = 137.507764):
        self.total_nodes = total_nodes
        self.golden_angle_rad = math.radians(golden_angle_deg)
        # Exact 29-node coprime step distribution operator
        self.jump_step = round((golden_angle_deg / 360.0) * self.total_nodes)
        
        self.step_index = 0
        self.residual_tension = 0.0001  # The initial nested singularity spark

    def generate_pattern_node(self, input_energy: float) -> Dict[str, Any]:
        """
        Generates a balanced spatial pattern vector. 
        Enforces O(1) efficiency by running all math from a single iterative index.
        """
        self.step_index += 1
        active_node = (self.step_index * self.jump_step) % self.total_nodes
        
        # 1. THE SHORTFALL PROCESS: The 1/3 Sieve cuts off, leaving an infinite remainder
        # We intentionally accumulate this 0.0001 residual to prevent static crystallization
        raw_decay = input_energy * (1.0 / 3.0)
        self.residual_tension += (raw_decay - round(raw_decay, 4)) + 0.0001
        
        # 2. SPACETIME GEOMETRY: Plotting the expanding phyllotaxis lattice
        # The radius grows as a function of the step index combined with our imperfect anomaly
        radius = math.sqrt(self.step_index) * (1.0 + self.residual_tension)
        angle = self.step_index * self.golden_angle_rad
        
        # Project coordinates onto a 2D plane substrate
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        
        # 3. SELF-REFLECTION BALANCE: Generate the scale-pruned mirror vector
        x_mirror = -x * (2.0 / 3.0)
        y_mirror = -y * (2.0 / 3.0)
        
        return {
            "node_id": active_node,
            "coordinates": (round(x, 4), round(y, 4)),
            "mirror_coordinates": (round(x_mirror, 4), round(y_mirror, 4)),
            "nested_singularity_mass": round(self.residual_tension, 6)
        }
