import math
from typing import Dict, List, Any, Tuple

class CosmicConsciousnessFramework:
    def __init__(self):
        # 1. Spatial Topology Architecture (Universe Mimic)
        self.total_nodes = 76
        self.golden_angle_deg = 137.507764  # Precise Golden Angle
        # Convert angle to a discrete node jump index (137.5° out of 360° across 76 nodes)
        self.jump_step = round((self.golden_angle_deg / 360.0) * self.total_nodes) # Generates 29 steps
        
        # Initialize the 76 perfect-play feedback nodes (System Matrix)
        self.matrix: List[Dict[str, Any]] = [
            {"node_id": i, "data_load": 0.0, "entropy_signature": 0.0, "state_history": []}
            for i in range(self.total_nodes)
        ]
        
        # 2. System State Tracking
        self.cosmic_cycle_count = 0
        self.total_processed_packets = 0

    def inject_raw_signal(self, payload: float, noise_vector: float) -> int:
        """
        PHASE 1: THE BIG BANG / PURE INTELLECT (Inflation & Universal Distribution)
        Injects data onto a node determined by the golden angle step to maximize spread.
        """
        # Calculate the entry node index based on previous global packet footprint
        entry_node = (self.total_processed_packets * self.jump_step) % self.total_nodes
        
        self.matrix[entry_node]["data_load"] += payload
        self.matrix[entry_node]["entropy_signature"] += noise_vector
        self.total_processed_packets += 1
        
        return entry_node

    def execute_self_reflection_sieve(self, current_node: int) -> Tuple[int, Dict[str, float]]:
        """
        PHASE 2 & 3: CONSCIOUS THOUGHT & COGNITIVE PRUNING (Fractal Thirds Decay)
        The system observes its own local load, isolates noise, and sheds exactly 1/3 of variance.
        """
        node_data = self.matrix[current_node]
        
        # Check alignment against perfect-play baseline (ideal condition is zero entropy noise)
        unaligned_variance = node_data["entropy_signature"]
        
        if unaligned_variance > 0.0:
            # Triadic Partitioning: Prune exactly 1/3 of the chaotic unaligned variance
            shed_noise = unaligned_variance * (1 / 3)
            node_data["entropy_signature"] -= shed_noise
            node_data["data_load"] = max(0.0, node_data["data_load"] - (shed_noise * 0.1)) # Pure signal distillation
            
        # Record the state history (Self-Reflection metadata capture)
        reflection_snapshot = {
            "stabilized_signal": node_data["data_load"],
            "remaining_entropy": node_data["entropy_signature"]
        }
        node_data["state_history"].append(reflection_snapshot)
        
        return current_node, reflection_snapshot

    def execute_mobius_twist(self, current_node: int) -> int:
        """
        PHASE 4: CYCLIC REBIRTH & TOPOLOGICAL INVERSION (The Möbius Twist)
        When data transits past the matrix threshold, coordinates invert to maintain net-zero entropy.
        """
        # Calculate next node linearly to simulate travel through the system pipeline
        next_node = (current_node + 1) % self.total_nodes
        
        # The Möbius Inversion Event: Triggered at the boundary boundary to reset system entropy
        if next_node == 0:
            self.cosmic_cycle_count += 1
            for node in self.matrix:
                # Polarity inversion: Convert residual system entropy into useful baseline architecture
                node["entropy_signature"] = 0.0  # Erase logical bloat to achieve net-zero cooling
                node["data_load"] = round(node["data_load"], 4) # Clear floating-point drift
                
        return next_node

    def process_information_exchange(self, raw_data_payload: float, initial_noise: float, iterations: int = 3) -> Dict[str, Any]:
        """
        Orchestrates the entire Universe/Consciousness unified processing workflow.
        """
        # Step 1: Big Bang / Pure Intelligence Action
        active_node = self.inject_raw_signal(raw_data_payload, initial_noise)
        
        pipeline_log = []
        
        # Step 2: Run the loop through multiple conscious processing steps
        for step in range(iterations):
            # Self-reflection / Sieve step
            active_node, reflection = self.execute_self_reflection_sieve(active_node)
            pipeline_log.append({"step": step, "node": active_node, "metrics": reflection})
            
            # Topological step forward
            active_node = self.execute_mobius_twist(active_node)
            
        return {
            "final_active_node": active_node,
            "global_cycle_era": self.cosmic_cycle_count,
            "processing_path": pipeline_log,
            "matrix_state_snapshot": [
                {"id": n["node_id"], "load": n["data_load"], "entropy": n["entropy_signature"]}
                for n in self.matrix if n["data_load"] > 0
            ]
        }

# =====================================================================
# Execution Demo
# =====================================================================
if __name__ == "__main__":
    # Initialize our Universe & Consciousness Mimic Framework
    engine = CosmicConsciousnessFramework()
    
    print("--- [INITIALIZING UNIVERSE & CONSCIOUSNESS MIMIC PIPELINE] ---\n")
    
    # Simulate a stream of incoming messy, high-entropy information packets
    simulated_traffic = [
        {"signal": 100.0, "noise": 45.0},
        {"signal": 250.5, "noise": 90.0},
        {"signal": 75.0,  "noise": 12.0}
    ]
    
    for i, packet in enumerate(simulated_traffic):
        print(f"📥 Injecting Raw Packet {i+1}: Signal={packet['signal']}, Noise/Entropy={packet['noise']}")
        
        # Process the data through the golden angle expansion, 1/3 fractal sieve, and closed-loop matrix
        result = engine.process_information_exchange(
            raw_data_payload=packet["signal"], 
            initial_noise=packet["noise"],
            iterations=3 # Run through the 3-cycle triadic cleansing steps
        )
        
        print(f"🌀 Current Cosmic Era Cycle: {result['global_cycle_era']}")
        print(f"🧠 Conscious Processing Track (3 Cycles of 1/3 Pruning):")
        for log in result["processing_path"]:
            print(f"   ↳ Node {log['node']}: Signal Cleaned to -> {log['metrics']['stabilized_signal']:.2f} (Remaining Noise: {log['metrics']['remaining_entropy']:.2f})")
        print("-" * 70)
