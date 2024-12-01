

class TabsFormatter():
    def __init__(self, riff, tuning_notes):
        self.riff = riff
        self.tuning_notes = tuning_notes

    def format(self):
        tabs = [f"{string}|" for string in self.tuning_notes]
        #tabs = ["E|", "B|", "G|", "D|", "A|", "E|"]
        for note in self.riff:
            for i in range(0, len(tabs)):
                if i == 5:
                    tabs[i] += f"{note}--"
                else:
                    tabs[i] += "---"
        return tabs


    