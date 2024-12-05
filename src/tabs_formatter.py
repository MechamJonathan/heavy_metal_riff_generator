

class TabsFormatter():
    def __init__(self, riff, tuning_notes):
        self.riff = riff
        self.tuning_notes = tuning_notes

    def format(self):
        tabs = [f"{string}|" for string in self.tuning_notes]
        for bar in self.riff:
            for beat in bar:

                if isinstance(beat, list):  # Power chord
                    for i, (string_index, fret) in enumerate(beat):
                        if len(fret) == 2:  # Two-digit fret
                            tabs[string_index] += f"{fret}-"
                        else:  # One-digit fret
                            tabs[string_index] += f"{fret}--"


                    for i in range(len(tabs)):
                        if i not in [note[0] for note in beat]:
                            tabs[i] += "---"

                elif beat is None:  # Rest or silence
                    for i in range(len(tabs)):
                        tabs[i] += "---"
                else:
                    string_index, note = beat
                    for i in range(len(tabs)):
                        if i == string_index:
                            tabs[i] += f"{note}--"  # Add the note to the correct string
                        else:
                            tabs[i] += "---"  # Add dashes for other strings

            for i in range(len(tabs)):
                tabs[i] += "|"
    
        return tabs[::-1]

    