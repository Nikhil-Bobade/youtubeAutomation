import os ,random
from pydub import AudioSegment


def smooth_fade_mixtape(folder,output,transition_ms=6000):
    files=[f for f in os.listdir(folder) if f.endswith(("mp3","wav")) ]
    random.shuffle(files)

    mixtape=None


    for file in files:
        song=AudioSegment.from_file(os.path.join(folder,file))
        song=song.set_channels(2).set_frame_rate(44100)

        if mixtape is None:
            mixtape=song

        else:

            overlap=min(transition_ms,len(song),len(mixtape))
            outgoing=mixtape[-overlap:].fade_out(overlap).low_pass_filter(4000)
            incoming=song[:overlap].fade_in(overlap).low_pass_filter(4000)
            transition=outgoing.overlay(incoming)
            mixtape=mixtape[:-overlap]+transition+song[overlap:]


    mixtape.export(output,format="mp3")
    return output

            
