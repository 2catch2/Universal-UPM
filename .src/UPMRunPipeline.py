import os
from UPMDataEncoder import UPMDataEncoder
from UPMSpacetimeGenerator import UPMSpacetimeGenerator
from UPMTopologicalManifold import UPMTopologicalManifold

class UniversalUPMPipeline:
    """
    UPMv1.04-PIPE: Master System Pipeline Orchestrator.
    Interconnects the data encoder, spacetime generator, and topological manifold
    into a functional end-to-end information exchange interface.
    """
    def __init__(self):
        # Instantiate and interconnect the modular engine architectures
        self.encoder = UPMDataEncoder()
        self.spacetime = UPMSpacetimeGenerator()
        self.manifold = UPMTopologicalManifold()
        
    def process_text_payload(self, text_input: str) -> dict:
        """ Runs a single string transaction through the complete system matrix. """
        # Step 1: Text-to-Vector Transmutation (Encoding)
        encoded_vectors = self.encoder.encode_text_string(text_input)
        signal = encoded_vectors["signal_payload"]
        noise = encoded_vectors["entropy_variance"]
        
        # Step 2: Environmental Coordinate Generation (Spacetime Grid)
        # Using signal mass as the structural input energy
        spacetime_quantum = self.spacetime.generate_spacetime_quantum(energy_input=signal)
        spatial_coordinates = spacetime_quantum["spatial_metrics"]["primary_space"]
        
        # Step 3: Topological Fault-Tolerant Braiding (Manifold Execution)
        node_id, knot_stability = self.manifold.execute_topological_braid(signal=signal, noise=noise)
        
        return {
            "input_string": text_input,
            "distilled_metrics": {
                "signal_mass": signal,
                "entropy_noise": noise
            },
            "generated_space": spatial_coordinates,
            "braid_target_node": node_id,
            "global_knot_integrity": f"{knot_stability * 100:.2f}%"
        }

    def process_external_text_file(self, file_path: str):
        """
        Interconnecting helper: Reads an external text document, processes it line by line,
        and pipes it into the active topological manifold.
        """
        if not os.path.exists(file_path):
            print(f"⚠️ File Not Found: Creating dummy file at '{file_path}' for simulation stability.")
            with open(file_path, "w") as f:
                f.write("Universal Process Mimic Initialized.\nGeometry creates balance.\nEntropy returns to net-zero.")

        print(f"📖 Streaming data from file substrate: '{file_path}'\n")
        
        with open(file_path, "r") as file:
            lines = file.readlines()
            
        for index, line in enumerate(lines):
            clean_line = line.strip()
            if not clean_line:
                continue
                
            transaction = self.process_text_payload(clean_line)
            print(f"🧵 Line {index+1} Processed Loop:")
            print(f"   ↳ Content: \"{transaction['input_string']}\"")
            print(f"   ↳ Space Vector Coordinate: {transaction['generated_space']}")
            print(f"   ↳ Woven onto Torus Node: {transaction['braid_target_node']} | Global System Stability: {transaction['global_knot_integrity']}")
            print("-" * 75)

# =====================================================================
# Pipeline Operations Check
# =====================================================================
if __name__ == "__main__":
    print("⚡ [UPM MASTER PIPELINE RUNNING] ⚡")
    print("System Matrix status: Interconnected and Online.\n")
    
    # Initialize the interconnected orchestration core
    pipeline_manager = UniversalUPMPipeline()
    
    # Target file name to showcase external data streaming interconnectivity
    target_data_file = "cosmic_input_stream.txt"
    
    # Run the continuous file pipeline process
    pipeline_manager.process_external_text_file(target_data_file)
