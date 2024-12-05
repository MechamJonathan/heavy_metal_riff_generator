
# low_E = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]

# tunings = {
#             "Standard_E": ["E", "A", "D", "G", "B", "E"],
#             "Drop_D": ["E", "B", "G", "D", "A", "D"]
#         }

# strings = {
#             "Standard_E" : [["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"], # Low E
#                             ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"], # A string
#                             ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#"], # D string
#                             ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#"]  # G string
#                              ]
# }

class Tuning():
    tunings = {
            "Standard_E": ["E", "A", "D", "G", "B", "E"],
            "Drop_D": ["E", "B", "G", "D", "A", "D"]
        }

    strings = {
                "Standard_E" : [["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"], # Low E
                                ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"], # A string
                                ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#"], # D string
                                ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#"]  # G string
                                ]
}
    def __init__(self, tuning_name):
        self.tuning_name = tuning_name
        self.tunings = self.tunings[tuning_name]
        self.strings = self.strings[tuning_name]

    def __repr__(self):
        return f"Tuning: {self.tuning_name}"

    def get_tuning(self):
        return self.tunings

    def get_tuning_name(self):
        return self.tuning_name


    