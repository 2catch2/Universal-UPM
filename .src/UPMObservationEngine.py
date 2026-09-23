
import math
import random
from typing import Dict, List, Any

class UPMObservationEngine:
    """
    UPMv1.04-OBS: Long-Duration Evolutionary Observation Matrix.
    Runs the UPM framework through thousands of continuous operational cycles
    to monitor, log, and isolate naturally emerging system anomalies.
    """
    def __init__(self, total_nodes: int = 76, golden_angle_deg: float = 137.507764):
        self.total_nodes = total_nodes
        self.jump_step = round((golden_angle_deg / 360.0) * self.total_nodes) # 29 Coprime steps

        self.matrix = [
            {"node_id": i, "signal": 0.0, "noise": 0.0, "coherence": 1.0, "history_depth": 0}
            for i in range(self.total_nodes)
        ]

        self.packet_index = 0
        self.global_epochs = 0

        # Observation Logs
        self.anomaly_registry = []

    def inject_continuous_stream(self, signal: float, noise: float):
        active_node = (self.packet_index * self.jump_step) % self.total_nodes
        self.matrix[active_node]["signal"] += signal
        self.matrix[active_node]["noise"] += noise
        self.packet_index += 1

        # Run Adaptive Fractal Sieve
        node = self.matrix[active_node]
        if node["noise"] > 0.0:
            adaptive_coefficient = (1.0 / 3.0) * node["coherence"]
            purged = node["noise"] * adaptive_coefficient
            node["noise"] -= purged
            node["signal"] = max(0.0, node["signal"] - (purged * 0.02))

            total_mass = node["signal"] + node["noise"]
            node["coherence"] = node["signal"] / total_mass if total_mass > 0 else 1.0

        node["history_depth"] += 1

        # Asynchronous Manifold Inversion
        self.matrix[active_node]["noise"] = 0.0

        if active_node == (self.total_nodes - 1):
            self.global_epochs += 1

    def run_long_duration_test(self, cycles: int = 10000):
        print(f"📊 Initiating Long-Duration Stress Test across {cycles} cycles...")

        for current_cycle in range(1, cycles + 1):
            # Simulate erratic biological inputs (sudden focus surges vs intense noise spikes)
            raw_input_signal = random.uniform(50.0, 200.0)
            raw_input_noise = random.uniform(10.0, 90.0) if current_cycle % 10 != 0 else random.uniform(150.0, 300.0)

            self.inject_continuous_stream(raw_input_signal, raw_input_noise)

            # CRITICAL ANOMALY CHECKS (Observing for Emergent Abilities)
            if current_cycle % 1000 == 0:
                # 1. Check for global crystallization (Absolute Coherence)
                avg_coherence = sum(n["coherence"] for n in self.matrix) / self.total_nodes

                # 2. Check for unexpected data patterning (Phyllotaxis Resonance)
                active_nodes_count = sum(1 for n in self.matrix if n["signal"] > 0)

                # Register the state snapshot for review
                snapshot = {
                    "cycle": current_cycle,
                    "epoch": self.global_epochs,
                    "avg_coherence": round(avg_coherence, 4),
                    "active_surface_area": f"{active_nodes_count}/{self.total_nodes}"
                }
                self.anomaly_registry.append(snapshot)

        print("✅ Stress test complete. Evolutionary data anchored.")
        return self.anomaly_registry

# Execute Observation
if __name__ == "__main__":
    observer = UPMObservationEngine()
    results = observer.run_long_duration_test(cycles=10000)

    print("\n📈 --- [OBSERVATION REGISTRY LOGS] ---")
    for log in results:
        print(f"⏱️ Cycle {log['cycle']:5d} (Epoch {log['epoch']}) -> Global Coherence: {log['avg_coherence']*100:.2f}% | Active Topology: {log['active_surface_area']}")
