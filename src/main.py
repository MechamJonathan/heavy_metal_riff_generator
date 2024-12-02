
from riff import Riff
from scale import Scale
from tuning import Tuning
from tabs_formatter import TabsFormatter


def main():
    print("\nWelcome to the Simple Guitar Riff Generator\n")
    key = input("Please choose a key (E): ").strip() or "E"
    scale_type = input("Please choose a scale (Minor): ").strip() or "Minor"
    tuning = input("Please choose a tuning:") or "Standard_E"

    chosen_scale = Scale(key, scale_type)
    chosen_scale_notes = chosen_scale.get_scale()
    chosen_tuning = Tuning(tuning)
    tuning_notes = chosen_tuning.get_tuning()

    riff = Riff(chosen_scale_notes, chosen_tuning).generate_bar_chords()
    tabs = TabsFormatter(riff, tuning_notes)

    print("\nGenerated Riff:\n")
    print(chosen_scale)
    print(chosen_tuning)
    print(f"{riff}\n")
    print("\n".join(tabs.format()))

if __name__ == '__main__':
    main()