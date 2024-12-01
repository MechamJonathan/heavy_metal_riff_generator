
low_E = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]

class Tuning():
    def __init__(self, tuning_name):
        self.tuning_name = tuning_name
        self.tunings = {
            "Standard_E": ["E", "A", "D", "G", "B", "E"],
            "Drop_D": ["D", "A", "D", "G", "B", "E"]
        }
        self.strings = None

    def __repr__(self):
        return f"Tuning: {self.tuning_name}"

    def get_tuning(self):
        return self.tunings.get(self.tuning_name, self.tunings["Standard_E"])

    def get_tuning_name(self):
        return self.tuning_name