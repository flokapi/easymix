


import easymix as mixer
import pydub
import time



def liveMix():
    mixer.play('01.mp3')
    for i in range(5):
        mixer.play('02.mp3')
        time.sleep(2)

    mixer.stop()


def liveMixPydub():
    sound01 = pydub.AudioSegment.from_file('01.mp3')
    sound02 = pydub.AudioSegment.from_file('02.mp3')

    mixer.play(sound01)
    for i in range(5):
        mixer.play(sound02)
        time.sleep(2)

    mixer.stop()


if __name__ == '__main__':
    liveMix()
    liveMixPydub()



