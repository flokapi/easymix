


import easymix as mixer
import pydub






def composeTrack():
    track = mixer.Track()
    track.addSound('01.mp3', 1.0)
    for t in range(5):
        track.addSound('02.mp3', t)

    track.save('track.mp3')


def composeTrackPydub():
    sound01 = pydub.AudioSegment.from_file('01.mp3')
    sound02 = pydub.AudioSegment.from_file('02.mp3')

    track = mixer.Track()
    track.addSound(sound01, 1.0)
    for t in range(5):
        track.addSound(sound02, t)

    track.save('track_pydub.mp3')


if __name__ == '__main__':
    composeTrack()
    composeTrackPydub()


