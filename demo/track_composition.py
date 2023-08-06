


import easymix as mixer
import pydub




milisec = 1000


def composeTrack():
    track = mixer.Track()
    track.addSound('01.mp3', 1000*milisec)
    for i in range(5):
        track.addSound('02.mp3', i*1000*milisec)

    track.save('track.mp3')


def composeTrackPydub():
    sound01 = pydub.AudioSegment.from_file('01.mp3')
    sound02 = pydub.AudioSegment.from_file('02.mp3')

    track = mixer.Track()
    track.addSound(sound01, 1000*milisec)
    for i in range(5):
        track.addSound(sound02, i*1000*milisec)

    track.save('track_pydub.mp3')


if __name__ == '__main__':
    composeTrack()
    composeTrackPydub()


