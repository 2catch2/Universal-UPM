import json
import math
from typing import List, Dict, Any

class UPMVisualizerLink:
    """
    UPMv1.04-VIS: Visualizer Export and Rendering Link.
    Converts 76-node toroidal coordinate paths into standard visualization 
    payloads and renders mathematical wireframe plots.
    """
    def __init__(self, major_radius_R: float = 10.0, minor_radius_r: float = 3.0):
        # Toroidal parameters for 3D coordinate space mappings
        self.R = major_radius_R  # Distance from center of donut tube to center of donut hole
        self.r = minor_radius_r  # Radius of the inner tube itself

    def map_flat_index_to_3d_torus(self, node_id: int, total_nodes: int = 76) -> tuple:
        """
        Transforms a linear 76-node matrix index into precise (X, Y, Z) 
        coordinates wrapped tightly on a 3D torus surface.
        """
        # Major angle theta: wraps around the large ring circumference
        theta = (2.0 * math.pi * node_id) / total_nodes
        
        # Minor angle phi: winds through the inner tube (simulating the Möbius loop factor)
        # Using your 29-step jump as a winding frequency multiplier
        phi = theta * (29.0 / 76.0) * 2.0 * math.pi
        
        # Standard parametric parametric formulas for a 3D Torus surface
        x = (self.R + self.r * math.cos(phi)) * math.cos(theta)
        y = (self.R + self.r * math.cos(phi)) * math.sin(theta)
        z = self.r * math.sin(phi)
        
        return (round(x, 4), round(y, 4), round(z, 4))

    def export_pipeline_to_json(self, pipeline_history: List[Dict[str, Any]], output_file: str = "upm_render_data.json"):
        """
        Converts active pipeline transaction maps into clean, structured JSON format
        ready for direct ingestion into JavaScript, Blender, or web-based engines.
        """
        formatted_points = []
        for index, step in enumerate(pipeline_history):
            node_id = step.get("braid_target_node", 0)
            x, y, z = self.map_flat_index_to_3d_torus(node_id)
            
            formatted_points.append({
                "sequence_index": index,
                "node_id": node_id,
                "string_preview": step.get("input_string", ""),
                "coordinates_3d": {"x": x, "y": y, "z": z},
                "knot_integrity": step.get("global_knot_integrity", "0.0%")
            })
            
        with open(output_file, "w") as f:
            json.dump(formatted_points, f, indent=4)
        print(f"💾 Vector export complete! Toroidal path data saved to: '{output_file}'")

    def execution_local_render_demo(self, node_sequence: List[int]):
        """
        Fallback analytical visualization text-mapper. Prints structural 
        3D coordinate mappings when heavy external GUI engines are detached.
        """
        print("\n📐 --- [TOROIDAL XYZ MATRIX COORDINATE LOGS] ---")
        for idx, node in enumerate(node_sequence):
            x, y, z = self.map_flat_index_to_3d_torus(node)
            print(f"🧵 Vector Point {idx+1} (Node {node:2d}) -> X: {x:7.4f} | Y: {y:7.4f} | Z: {z:7.4f}")

if __name__ == "__main__":
    print("🎨 [UPM VISUALIZER LINK CORE ONLINE]")
    visualizer = UPMVisualizerLink()
    
    # Simulate a 29-step golden angle jump node sequence output from your pipeline
    simulated_node_route = [0, 29, 58, 11, 40]
    visualizer.execution_local_render_demo(simulated_node_route)
