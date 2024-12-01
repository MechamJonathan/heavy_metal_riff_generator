import random
from tuning import low_E

class Riff():
    def __init__(self, scale_notes, tuning_notes=""):
        self.scale_notes = scale_notes
        self.tuning_notes = tuning_notes
        self.rhythm_patterns = [
        [1, 0, 1, 0, 1, 0, 1, 1], #fat chugs
        [1, 0, 1, 1, 0, 1, 0, 1]  #syncropated
        ]


    def generate(self):
        #scale_notes = self.scale[f"{self.key}_{self.scale}"]
        riff = []
        rhythm = random.choice(self.rhythm_patterns)

        for beat in rhythm:
            if beat == 1:
                note = random.choice(self.scale_notes)
                riff.append(low_E.index(note))

            else:
                riff.append(0)
        return riff



# def generate_metal_riff(key, scale):
#     scale_notes = scales[f"{key}_{scale}"]
#     riff = []
#     rhythm = random.choice(rhythm_patterns)
#     for beat in rhythm:
        
#         if beat == 1:
#             note = random.choice(scale_notes)
#             riff.append(low_E.index(note))

#         else:
#             riff.append(0)
#     return riff


# def to_tabs(riff):
#     tabs = ["E|", "B|", "G|", "D|", "A|", "E|"]
#     for note in riff:
#         for i in range(0, len(tabs)):
#             if i == 5:
#                 tabs[i] += f"{note}--"
#             else:
#                 tabs[i] += "---"
#     return tabs






# def generate_riff(key="E", scale="Minor", tuning="Standard_E"):
#     scale_notes = scales.get(f"{key}_{scale}", scales["E_Minor"])
#     #guitar_tuning = tunings.get(f"{tuning}", tunings["Standard"])

#     riff = []
#     for _ in range(4): #4 beats per measure
#         bar = []
#         for beat in rhythm_patterns[random.randint(0, len(rhythm_patterns) - 1)]:
#             if beat == 1:
#                 note = random.choice(scale_notes)
#                 bar.append(note)
#             else:
#                 bar.append("-")
#         riff.append(bar)
#     return riff

# def generate_tabs(riff):
#     tablature = ["E|", "B|", "G|", "D|", "A|", "E|"]
#     for bar in riff:
#         for i, note in enumerate(bar):
#             tablature[i] += f"{note}--"
#     return tablature
    

