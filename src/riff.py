import random

class Riff():
    def __init__(self, scale_notes, tuning):
        self.scale_notes = scale_notes
        self.tuning = tuning
        self.rhythm_patterns = [
        [1, 0, 1, 0, 1, 0, 1, 1], #fat chugs
        [1, 0, 1, 1, 0, 1, 0, 1]  #syncropated
        ]


    def generate(self):
        riff = []
        pattern = random.choice(self.rhythm_patterns) 

        bar = [] 
        for beat in pattern:
            if beat == 1: 
                string_index = random.randint(0, 2)
                note = random.choice(self.scale_notes)
                bar.append((string_index, self.tuning.strings[string_index].index(note)))
            else:
                bar.append((0, 0))

        riff.append(bar)
        return riff

    def generate_bar_chords(self):
        riff = []
        pattern = random.choice(self.rhythm_patterns) 

        for _ in range(2):
            bar = []
            for beat in pattern:
                if beat == 1: 
                    root_string = random.randint(0, len(self.tuning.strings) - 3)
                    bar_chord_fret = random.randint(0, 11) 

                    bar_chord = [
                        (root_string, f"{bar_chord_fret}"),         
                        (root_string + 1, f"{bar_chord_fret + 2}"),      
                        (root_string + 2, f"{bar_chord_fret + 2}"),       
                    ]
                    bar.append(bar_chord) 

                else:  
                    bar.append((0,0))
            riff.append(bar) 

        return riff