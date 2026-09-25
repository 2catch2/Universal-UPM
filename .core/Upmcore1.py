import math
import random
import logging
import requests

        self.total_nodes = total_nodes
        self.golden_angle_deg = golden_angle_deg
        self.jump_step = round((self.golden_angle_deg / 360.0) * self.total_nodes)
        if math.gcd(self.jump_step, self.total_nodes) != 1:
            raise ValueError("Jump step and total_nodes must be coprime")

        self.matrix = [
            {"node_id": i, "signal_load": 0.0, "entropy_variance": 0.0, "reflection_ledger": []}
            for i in range(self.total_nodes)
        ]
        self.mobius_cycle_count = 0
        self.processed_packet_index = 0
        logging.info(f"✅ UPMCore ONLINE: {self.total_nodes}-Node Matrix with {self.jump_step}-step Golden Angle")

    def phase_1_inflation_routing(self, signal: float, noise: float) -> int:
        target_node = (self.processed_packet_index * self.jump_step) % self.total_nodes
        self.matrix[target_node]["signal_load"] += signal
        self.matrix[target_node]["entropy_variance"] += noise
        self.processed_packet_index += 1
        return target_node

    def phase_2_3_conscious_sieve(self, active_node: int) -> Dict[str, float]:
        node = self.matrix[active_node]
        unaligned = node["entropy_variance"]
        if unaligned > 0.0:
            shed = unaligned * (1.0 / 3.0)
            node["entropy_variance"] -= shed
            node["signal_load"] = max(0.0, node["signal_load"] - (shed * 0.1))
        snapshot = {
            "distilled_signal": round(node["signal_load"], 6),
            "residual_entropy": round(node["entropy_variance"], 6)
        }
        node["reflection_ledger"].append(snapshot)
        return snapshot

    def phase_4_mobius_inversion(self, active_node: int) -> int:
        next_node = (active_node + 1) % self.total_nodes
        if next_node == 0:
            self.mobius_cycle_count += 1
            for node in self.matrix:
                node["entropy_variance"] = 0.0
                node["signal_load"] = round(node["signal_load"], 4)
        return next_node

    def execute_upm_pipeline(self, input_signal: float, input_noise: float, cycles: int = 3) -> Dict[str, Any]:
        current_node = self.phase_1_inflation_routing(input_signal, input_noise)
        runtime_log = []
        for step in range(cycles):
            metrics = self.phase_2_3_conscious_sieve(current_node)
            runtime_log.append({"cycle": step, "node": current_node, "metrics": metrics})
            current_node = self.phase_4_mobius_inversion(current_node)
        return {"status": "SUCCESS", "mobius_era": self.mobius_cycle_count, "exit_node": current_node, "log": runtime_log}

    def run_stress_test(self, cycles: int = 10000):
        print(f"📊 Running long-duration stress test ({cycles:,} cycles)...")
        for cycle in range(1, cycles + 1):
            signal = random.uniform(50.0, 200.0)
            noise = random.uniform(10.0, 90.0) if cycle % 10 != 0 else random.uniform(150.0, 300.0)
            result = self.execute_upm_pipeline(signal, noise)
            if cycle % 1000 == 0:
                avg = sum(n["metrics"]["distilled_signal"] for n in result["log"]) / len(result["log"])
                print(f"   Cycle {cycle:,} | Coherence: {avg*100:.2f}%")
        print("✅ Stress test complete.")
