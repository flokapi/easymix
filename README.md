# Usage

Live Audio Mixer

```python
import easymix as mixer
import time

def liveMix():
    mixer.play('01.mp3')
    for i in range(5):
        mixer.play('02.mp3')
        time.sleep(2)

    mixer.stop()
```



Compose Audio track

```python
import easymix as mixer

def composeTrack():
    track = mixer.Track()
    track.addSound('01.mp3', 1.0)
    for t in range(5):
        track.addSound('02.mp3', t)

    track.save('track.mp3')
```



You can also define the sounds as `pydub` audio segments. It's convenient in case you need to apply effects on the sounds before playing, such as volume adjustment.

```python
import pydub

sound01 = pydub.AudioSegment.from_file('01.mp3')

sound01 -= 5	# reduce 5dB

...
mixer.play(sound01)

...
track.addSound(sound01, 1.0)
```





# Setup

Install pip package

```
pip3 install easymix
```





# Known issues

This is only a prototype. Beware of the following issues which require proper investigation:

1. The `pyaudio` package installation fails with Python 3.11.4, but works with Python 3.9.2.
2. The sounds might be played at higher speed than expected (bit rate issue)
