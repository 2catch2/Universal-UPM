import math
from typing import Dict, Any, List

class UPMDataEncoder:
    """
    UPMv1.04-ENC: Universal Process Mimic Data Encoder.
    Transmutes alphanumeric text inputs into geometric Signal and Entropy matrices
    ready for execution within the 76-node toroidal architecture.
    """
    def __init__(self):
        # A simple, eco-efficient weighting map based on character categories
        # Vowels hold baseline resonance, consonants provide physical load
        self.vowels = set("aeiouAEIOU")
        
    def encode_text_string(self, text: str) -> Dict[str, float]:
        """
        Converts an incoming string into raw UPM parameter payloads.
        Maintains O(N) linear parsing efficiency.
        """
        if not text:
            return {"signal_payload": 0.0, "entropy_variance": 0.0}
            
        total_ascii_sum = 0
        consonant_mass = 0.0
        vowel_resonance = 0.0
        entropy_noise_score = 0.0
        
        for char in text:
            char_code = ord(char)
            total_ascii_sum += char_code
            
            # 1. SIGNAL PROCESSING: Determine structural information load
            if char.isalpha():
                if char in self.vowels:
                    vowel_resonance += char_code * 1.1
                else:
                    consonant_mass += char_code * 1.3
            # 2. ENTROPY PROCESSING: Divergent vectors (spaces, numbers, symbols) generate variance
            elif char.isspace():
                entropy_noise_score += 25.0  # Structured intervals
            else:
                entropy_noise_score += char_code * 1.5  # Chaotic spikes (punctuation/symbols)
                
        # Calculate balanced global metrics
        base_signal = (consonant_mass + vowel_resonance) / len(text)
        
        # Balance scale check: Make sure entropy forms a natural ratio relative to the content depth
        calculated_entropy = (entropy_noise_score / total_ascii_sum) * 100.0 if total_ascii_sum > 0 else 0.0
        
        return {
            "input_preview": text[:30] + "..." if len(text) > 30 else text,
            "signal_payload": round(base_signal, 4),
            "entropy_variance": round(calculated_entropy, 4)
        }

    def batch_encode_data_stream(self, data_stream: List[str]) -> List[Dict[str, float]]:
        """Splits larger data arrays or logs into individual UPM packets."""
        return [self.encode_text_string(packet) for packet in data_stream]

# =====================================================================
# Functional Integrity Check
# =====================================================================
if __name__ == "__main__":
    encoder = UPMDataEncoder()
    print("📥 [UPMv1.04-ENC DATA ENCODER ONLINE]")
    print("Testing alphanumeric text conversion tracking...\n")
    
    # Test cases demonstrating different signal-to-noise profiles
    test_phrases = [
        "Core design is functional.",           # Clean informational statement
        "WARNING: System Error 404!!! #Chaotic" # High-entropy text payload
    ]
    
    for phrase in test_phrases:
        payload = encoder.encode_text_string(phrase)
        print(f"📄 Raw Input: '{payload['input_preview']}'")
        print(f"   ↳ Distilled Signal Mass: {payload['signal_payload']}")
        print(f"   ↳ Extracted Entropy/Noise Vector: {payload['entropy_variance']}")
        print("-" * 65)
