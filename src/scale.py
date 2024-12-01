
class Scale():
    def __init__(self, key="E", scale_type="Minor"):
        self.key = key
        self.scale_type = scale_type
        self.scales = {
        "E_Minor": ["E", "F#", "G", "A", "B", "C", "D"]
        }
        self.notes = None   

    def __repr__(self):
        return f"Scale: {self.key}, {self.scale_type}"

    def get_scale(self):
        scale_key = f"{self.key}_{self.scale_type}"
        return self.scales.get(scale_key, self.scales["E_Minor"])  # Default to a known scale
    
    def get_key(self):
        return self.key