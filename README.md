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
    track.addSound('01.mp3', 1000*milisec)
    for i in range(5):
        track.addSound('02.mp3', i*1000*milisec)

    track.save('track.mp3')
```



You can also define the sounds a `pydub` audio segments. It's convenient in case you need to apply effects on the sounds before playing, such as volume adjustment.

```python
import pydub

sound01 = pydub.AudioSegment.from_file('01.mp3')

sound01 -= 5	# reduce 5dB

...
mixer.play(sound01)

...
track.addSound(sound01, 1000*milisec)
```





# Setup

Install pip package

```
pip3 install easymixer
```

