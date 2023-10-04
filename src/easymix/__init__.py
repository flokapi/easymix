

import pydub
import pyaudio

from threading import Thread
from queue import SimpleQueue


class Track:
    def __init__(self):
        self.track = pydub.AudioSegment.empty()

    def addSound(self, sound, timeStamp=0):
        if type(sound) == str:
            sound = pydub.AudioSegment.from_file(sound)

        trackDuration = self.track.duration_seconds
        soundDuration = sound.duration_seconds
        emptyDuration = timeStamp + soundDuration - trackDuration

        self.track += pydub.AudioSegment.silent(emptyDuration*1000)
        self.track = self.track.overlay(sound, position=timeStamp*1000)

    def save(self, fileName):
        self.track.export(fileName)


class Mixer(Track, Thread):
    def __init__(self):
        super().__init__()
        Thread.__init__(self)

        self.chunkMs = 5
        self.iface = pyaudio.PyAudio()
        self.stream = self.iface.open(format=8,
                                      channels=1,
                                      rate=92000,
                                      output=True)
        self.stream.write(b'\x00' * 10**4)

    def __del__(self):
        self.stream.close()
        self.iface.terminate()

    def playChunk(self):
        output = self.track[:self.chunkMs]
        self.track = self.track[self.chunkMs:]

        if output.duration_seconds*1000 < self.chunkMs/2:
            output += pydub.AudioSegment.silent(self.chunkMs)

        self.stream.write(output.raw_data)

    def stop(self):
        self.track = pydub.AudioSegment.empty()

    def run(self):
        while True:
            if not queue.empty():
                sound = queue.get()
                self.addSound(sound)
            self.playChunk()


def play(sound):
    queue.put(sound)


def stop():
    mixer.stop()


queue = SimpleQueue()

mixer = Mixer()
mixer.start()
