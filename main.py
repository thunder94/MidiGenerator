import argparse
from random import randint
from miditime.miditime import MIDITime

class MIDI_Generator:
    first_octave = {'C': 24, 'C#': 25, 'D': 26, 'D#': 27, 'E': 28, 'F': 29, 'F#': 30, 'G': 31, 'G#': 32, 'A': 33,
                    'A#': 34, 'B': 35}
    second_octave = {'C': 36, 'C#': 37, 'D': 38, 'D#': 39, 'E': 40, 'F': 41, 'F#': 42, 'G': 43, 'G#': 44, 'A': 45,
                     'A#': 46, 'B': 47}
    third_octave = {'C': 48, 'C#': 49, 'D': 50, 'D#': 51, 'E': 52, 'F': 53, 'F#': 54, 'G': 55, 'G#': 56, 'A': 57,
                    'A#': 58, 'B': 59}
    fourth_octave = {'C': 60, 'C#': 61, 'D': 62, 'D#': 63, 'E': 64, 'F': 65, 'F#': 66, 'G': 67, 'G#': 68, 'A': 69,
                     'A#': 70, 'B': 71}
    fifth_octave = {'C': 72, 'C#': 73, 'D': 74, 'D#': 75, 'E': 76, 'F': 77, 'F#': 78, 'G': 79, 'G#': 80, 'A': 81,
                    'A#': 82, 'B': 83}
    sixth_octave = {'C': 84, 'C#': 85, 'D': 86, 'D#': 87, 'E': 88, 'F': 89, 'F#': 90, 'G': 91, 'G#': 92, 'A': 93,
                    'A#': 94, 'B': 95}
    seventh_octave = {'C': 96, 'C#': 97, 'D': 98, 'D#': 99, 'E': 100, 'F': 101, 'F#': 102, 'G': 103, 'G#': 104,
                      'A': 105, 'A#': 106, 'B': 107}
    octaves = [first_octave, second_octave, third_octave, fourth_octave, fifth_octave, sixth_octave, seventh_octave]

    def create_midi_file(self, tempo, path):
        if path is not None:
            midi_file = MIDITime(tempo, path + '\supersong.mid')
        else:
            midi_file = MIDITime(tempo, 'supersong.mid')
        return midi_file

    def generate_key_notes(self, key):
        all_notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        intervals = [2, 4, 5, 7, 9, 11]
        key_index = all_notes.index(key)
        key_notes = [key]
        for i in intervals:
            key_notes.append(all_notes[(key_index + i) % 12])
        return key_notes

    def generate_midi_notes(self, input_octaves, all_octaves, key_notes):
        midi_notes = []
        for i in input_octaves:
            for k in key_notes:
                midi_notes.append(all_octaves[i - 1].get(k))
        return midi_notes

    def generate_song(self, midi_notes, note_num, velocity, pause, duration):
        song = []
        start_beat = 0
        mn_last_index = len(midi_notes) - 2
        for i in range(note_num):
            song.append([start_beat, midi_notes[randint(0, mn_last_index)], velocity, duration])
            start_beat = start_beat + duration + pause + 1
        song.append([start_beat, midi_notes[0], velocity, duration])
        return song

parser = argparse.ArgumentParser(description='MIDI file generator - output file: supersong.mid')
parser.add_argument('key', choices=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
                    help='Select desired key (A,A#,...,G#)')
parser.add_argument('octaves', nargs='*', type=int, choices=range(1, 8), help='Specify octaves to use (1-7)')
parser.add_argument('-n', '--note_num', type=int, choices=range(1, 1000), default=10,
                    help='Specify number of notes')
parser.add_argument('-t', '--tempo', type=int, choices=range(1, 2000), default=120, help='Tempo of the song (BPM)')
parser.add_argument('-v', '--velocity', type=int, choices=range(0, 128), default=127, help='Note velocity')
parser.add_argument('-pa', '--pause', type=int, choices=range(0, 100), default=0,
                    help='Pause between notes (beats)')
parser.add_argument('-d', '--duration', type=int, choices=range(1, 100), default=3, help='Note duration (beats)')
parser.add_argument('-p', '--path', help='Directory where file will be saved')
args = parser.parse_args()

midi_generator = MIDI_Generator()
midi_file = midi_generator.create_midi_file(args.tempo, args.path)
key_notes = midi_generator.generate_key_notes(args.key)
midi_notes = midi_generator.generate_midi_notes(args.octaves, midi_generator.octaves, key_notes)
song = midi_generator.generate_song(midi_notes, args.note_num, args.velocity, args.pause, args.duration)
midi_file.add_track(song)
midi_file.save_midi()