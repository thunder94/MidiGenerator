# MidiGenerator
This program generates MIDI file. User can specify key, number of notes, velocity, pause and song duration

## Running
### Prerequisites
Program requires miditime library. To install it use following command:
```
pip install miditime
```
### Program arguments
Mandatory agruments:
* ```key``` - target key of the melody
* ```octaves``` - number of octaves to use (1-7)

Additional arguments:
* ```-n``` or ```note_num``` - number of notes
* ```-t``` or ```tempo``` - tempo in BPS (beats per minute)
* ```-v``` or ```velocity``` - note velocity
* ```-pa``` or ```pause``` - duration of pauses
* ```-d``` or ```duration``` - duration of whole song (beats)
* ```-p``` or ```path``` - path where output file should be saved
